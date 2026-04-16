package org.export.controller;

import jakarta.annotation.Resource;
import lombok.extern.slf4j.Slf4j;
import org.export.limiter.ExportLimiter;
import org.export.service.ExportAsyncService;
import org.export.service.UserService;
import org.export.vo.UserExportVo;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author aengus
 */
@Slf4j
@RestController
@RequestMapping("/export")
public class ExportController {

    @Resource
    private ExportLimiter limiter;

    @Resource
    private ExportAsyncService asyncService;

    @Resource
    private UserService userService;

    @PostMapping("export_user")
    public String exportUser(@RequestHeader("lang") String lang) {
        String userId = "1001";
        if (!limiter.tryUser(userId)) {
            log.error("操作频繁");
            return "操作频繁";
        }
        if (!limiter.tryGlobal()) {
            log.error("操作频繁");
            return "系统繁忙";
        }
        Long taskId = System.currentTimeMillis();
        asyncService.exportAll(taskId, () -> userService.query(), UserExportVo.class, lang);
        return "任务ID：" + taskId;
    }
}
