package org.example.log.service;

import com.alibaba.fastjson2.JSON;
import io.micrometer.common.util.StringUtils;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.example.log.annotation.OperationLog;
import org.example.log.entity.OperationLogContext;
import org.example.log.entity.SysOperationLog;
import org.example.log.enums.OperateType;
import org.example.log.mapper.SysOperationLogMapper;
import org.example.log.utils.DiffUtils;
import org.example.log.utils.TraceIdUtils;
import org.slf4j.MDC;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@Service
@Slf4j
@RequiredArgsConstructor
public class OperationLogAsyncService {

    private final SysOperationLogMapper sysOperationLogMapper;

    @Async("operationLogExecutor")
    public void save(OperationLogContext ctx) {
        try {
            if (StringUtils.isNotBlank(ctx.getTraceId())) {
                MDC.put(TraceIdUtils.TRACE_ID, ctx.getTraceId());
            }
            Object beforeObj = ctx.getBeforeObj();
            Object afterObj = ctx.getAfterObj();

            OperationLog anno = ctx.getOperationLog();
            OperateType type = anno.type();

            SysOperationLog log = new SysOperationLog();
            if (type == OperateType.BATCH) {
                Map<String, Object> batchInfo = new HashMap<>();
                batchInfo.put("batch", true);
                batchInfo.put("condition", ctx.getParsedCondition());
                batchInfo.put("affectRows", ctx.getAffectRows());
                batchInfo.put("operator", ctx.getUsername());
                batchInfo.put("updateBy", LocalDateTime.now());
                log.setAfterValue(JSON.toJSONString(batchInfo));
            }else{
                // ====== after：INSERT / UPDATE 才有 ======
                if (type != OperateType.DELETE) {
                    log.setAfterValue(safeToJson(afterObj));
                }

                // ====== before：UPDATE / DELETE 才有 ======
                if (type != OperateType.INSERT) {
                    log.setBeforeValue(safeToJson(beforeObj));
                }

                // ====== diff：只在 UPDATE 且配置了字段 ======
               /* if (type == OperateType.UPDATE && beforeObj != null && afterObj != null && anno.fieldNames().length > 0) {
                    Map<String, String> fieldNameMap = convertFieldNameMap(anno.fieldNames());
                    Map<String, Map<String, Object>> diffMap = DiffUtils.diff(beforeObj, afterObj, fieldNameMap);
                    log.setDiffValue(JSON.toJSONString(diffMap));
                }*/
                // ====== diff：UPDATE ======
                if (type == OperateType.UPDATE && beforeObj != null && afterObj != null) {

                    Map<String, Map<String, Object>> diffMap;

                    // ① 指定字段 diff（老逻辑）
                    if (anno.fieldNames().length > 0) {
                        Map<String, String> fieldNameMap =
                                convertFieldNameMap(anno.fieldNames());
                        diffMap = DiffUtils.diff(beforeObj, afterObj, fieldNameMap);

                    }
                    // ② 自动 diff（新逻辑）
                    else {
                        diffMap = DiffUtils.diffAuto(beforeObj, afterObj);
                    }

                    if (!diffMap.isEmpty()) {
                        log.setDiffValue(JSON.toJSONString(diffMap));
                    }
                }

                if (ctx.getBizException() == null) {
                    log.setStatus(1);
                } else {
                    log.setStatus(0);
                    log.setErrorMessage(ctx.getBizException().getMessage());
                }
            }
            log.setModuleCode(anno.module());
            log.setModuleName(anno.moduleName());
            log.setOperateType(type.name());
            log.setOperateTypeName(anno.typeName());
            log.setTargetId(anno.targetId());
            log.setTargetName(anno.targetName());
            log.setCreatedBy(ctx.getUsername());
            log.setCreatedDate(LocalDateTime.now());
            log.setTraceId(ctx.getTraceId());
            sysOperationLogMapper.insert(log);
        } catch (Throwable e) {
            // 日志失败 ≠ 业务失败
            log.warn("【异步操作日志失败】{}", e.getMessage(), e);
        }finally {
            MDC.remove(TraceIdUtils.TRACE_ID);
        }
    }

    private Map<String, String> convertFieldNameMap(String[] arr) {
        Map<String, String> res = new HashMap<>();
        for (String s : arr) {
            if (s.contains(":")) {
                String[] kv = s.split(":");
                res.put(kv[0], kv[1]);
            }
        }
        return res;
    }

    /**
     * JSON 体量保护，避免日志把服务拖死
     */
    private String safeToJson(Object obj) {
        if (obj == null) {
            return null;
        }
        String json = JSON.toJSONString(obj);
        if (json.length() > 10_000) {
            return "{\"_skipped\":\"object too large\"}";
        }
        return json;
    }
}
