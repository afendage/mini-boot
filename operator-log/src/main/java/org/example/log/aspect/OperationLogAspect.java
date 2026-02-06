package org.example.log.aspect;

import cn.hutool.core.bean.BeanUtil;
import com.baomidou.mybatisplus.core.metadata.TableInfo;
import com.baomidou.mybatisplus.core.metadata.TableInfoHelper;
import io.micrometer.common.util.StringUtils;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.session.SqlSessionFactory;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.reflect.MethodSignature;
import org.example.log.annotation.OperationLog;
import org.example.log.entity.OperationLogContext;
import org.example.log.enums.OperateType;
import org.example.log.service.OperationLogAsyncService;
import org.example.log.utils.DynamicTableQuery;
import org.example.log.utils.SpELUtils;
import org.example.log.utils.TraceIdUtils;
import org.springframework.core.DefaultParameterNameDiscoverer;
import org.springframework.core.ParameterNameDiscoverer;
import org.springframework.stereotype.Component;

import java.sql.SQLException;
import java.util.Collection;
import java.util.LinkedHashMap;
import java.util.Map;

@Aspect
@Component
@RequiredArgsConstructor
@Slf4j
public class OperationLogAspect {

    private final SqlSessionFactory sqlSessionFactory;
    private final OperationLogAsyncService operationLogAsyncService;

    @Around("@annotation(operationLog)")
    public Object around(ProceedingJoinPoint jp, OperationLog operationLog) throws Throwable {

        Object result = null;
        Throwable bizException = null;

        Object beforeObj = null;
        Integer affectRows=1;
        try {
            /* =========================
             * ① BEFORE：只给 UPDATE / DELETE 用
             * ========================= */
            if (operationLog.type() != OperateType.INSERT
                    && operationLog.entity() != Void.class
                    && StringUtils.isNotBlank(operationLog.id())) {

                Object idVal = SpELUtils.parse(operationLog.id(), jp);
                if (idVal != null) {
                    beforeObj = loadDbData(operationLog.entity(), idVal);
                }
            }

            result = jp.proceed();
            if (result instanceof Integer) {
                affectRows = (Integer) result;
            }
            return result;

        } catch (Throwable ex) {
            bizException = ex;
            throw ex;

        } finally {
            try {
                /* =========================
                 * ② AFTER：永远来自方法参数
                 * ========================= */
                Object afterObj = null;
                //存在返回ID 则通过 返回值当 ID，回查 DB
                if (operationLog.type() == OperateType.INSERT
                        && operationLog.entity() != Void.class
                        && result != null) {
                    Object idVal = SpELUtils.parseRaw(operationLog.id(), jp, result);
                    if (idVal != null) {
                        afterObj = loadDbData(operationLog.entity(), idVal);
                    }
                } else {
                    //否则用传递过来的参数
                    afterObj = buildAfterFromArgs(jp);
                }
                String parsedCondition = parseCondition(operationLog, jp);
                OperationLogContext ctx = OperationLogContext.builder()
                        .operationLog(operationLog)
                        .beforeObj(beforeObj)
                        .afterObj(afterObj)
                        .bizException(bizException)
                        .username("auto:system")
                        .traceId(TraceIdUtils.getOrCreate())
                        .batch(isBatchOperation(jp))
                        .parsedCondition(parsedCondition)
                        .affectRows(affectRows)
                        .build();

                operationLogAsyncService.save(ctx);

            } catch (Throwable e) {
                log.warn("【操作日志保存失败】{}", e.getMessage(), e);
            }
        }
    }

    /* =====================================================
     * BEFORE 查询（DB）
     * ===================================================== */
    private Object loadDbData(Class<?> entityClass, Object id) throws SQLException {

        TableInfo tableInfo = TableInfoHelper.getTableInfo(entityClass);
        if (tableInfo == null) {
            return null;
        }

        DynamicTableQuery query = new DynamicTableQuery(sqlSessionFactory);
        Map<String, Object> map = query.queryOne(
                tableInfo.getTableName(),
                tableInfo.getKeyColumn(),
                id
        );

        if (map == null) {
            return null;
        }

        return BeanUtil.mapToBean(map, entityClass, true);
    }

    private boolean isBatchOperation(ProceedingJoinPoint jp) {
        for (Object arg : jp.getArgs()) {
            if (arg instanceof Collection) {
                return true;
            }
        }
        return false;
    }

    /**
     * AFTER = 参数名 → 参数值
     */
    private static final ParameterNameDiscoverer nameDiscoverer =
            new DefaultParameterNameDiscoverer();
    private Object buildAfterFromArgs(ProceedingJoinPoint jp) {

        MethodSignature signature = (MethodSignature) jp.getSignature();
        String[] paramNames = nameDiscoverer.getParameterNames(signature.getMethod());
        Object[] args = jp.getArgs();

        if (paramNames == null || args == null || paramNames.length != args.length) {
            return null;
        }

        Map<String, Object> after = new LinkedHashMap<>();
        for (int i = 0; i < paramNames.length; i++) {
            after.put(paramNames[i], args[i]);
        }
        return after;
    }

    private String parseCondition(OperationLog operatorLog, ProceedingJoinPoint jp) {
        String condition = operatorLog.condition();
        if (StringUtils.isBlank(condition)) {
            return null;
        }

        // 如果不包含 SpEL，直接返回
        if (!condition.contains("#")) {
            return condition;
        }

        try {
            // 把 "id in #ids" 解析成真实值
            Object value = SpELUtils.parseRaw(condition, jp);
            return value == null ? condition : value.toString();
        } catch (Exception e) {
            log.warn("condition SpEL 解析失败: {}", condition, e);
            return condition;
        }
    }

}
