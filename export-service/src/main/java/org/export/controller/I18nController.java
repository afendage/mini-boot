package org.export.controller;

import com.baomidou.mybatisplus.core.metadata.IPage;
import jakarta.annotation.Resource;
import org.export.entity.I18n;
import org.export.service.I18nService;
import org.springframework.web.bind.annotation.*;

/**
 * @author aengus
 */
@RestController
@RequestMapping("/i18n")
public class I18nController {

    @Resource
    private I18nService service;

    @PostMapping("/add")
    public String add(@RequestBody I18n entity) {
        service.add(entity);
        return "ok";
    }

    @PostMapping("/update")
    public String update(@RequestBody I18n entity) {
        service.update(entity);
        return "ok";
    }

    @DeleteMapping("/delete")
    public String delete(String id) {
        service.delete(id);
        return "ok";
    }

    @GetMapping("/get")
    public String get(String code, String lang) {
        return service.get(code, lang);
    }

    @GetMapping("/list")
    public IPage<I18n> page(IPage<I18n> page, I18n req) {
        return service.page(page,req);
    }
}
