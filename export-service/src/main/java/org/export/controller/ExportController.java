package org.export.controller;

import org.export.limiter.ExportLimiter;
import org.export.service.ExportAsyncService;
import org.export.service.UserService;
import org.export.vo.UserExportVo;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;

@RestController
@RequestMapping("/export")
public class ExportController {

    @Resource
    private ExportLimiter limiter;

    @Resource
    private ExportAsyncService asyncService;

    @Resource
    private UserService userService;

    @PostMapping
    public String export(@RequestHeader("lang") String lang) {
        String userId = "1001";
        if (!limiter.tryUser(userId)) {
            return "操作频繁";
        }
        if (!limiter.tryGlobal()) {
            return "系统繁忙";
        }
        Long taskId = System.currentTimeMillis();
        asyncService.export(taskId, page -> userService.query(), UserExportVo.class, lang);
        return "任务ID：" + taskId;
    }
}
