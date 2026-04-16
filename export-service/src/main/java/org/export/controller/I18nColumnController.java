package org.export.controller;

import com.baomidou.mybatisplus.core.metadata.IPage;
import jakarta.annotation.Resource;
import org.export.entity.I18nColumn;
import org.export.service.ColumnI18nService;
import org.springframework.web.bind.annotation.*;

/**
 * @author aengus
 */
@RestController
@RequestMapping("/i18nColumn")
public class I18nColumnController {

    @Resource
    private ColumnI18nService service;

    @PostMapping("/add")
    public String add(@RequestBody I18nColumn entity) {
        service.add(entity);
        return "ok";
    }

    @PostMapping("/update")
    public String update(@RequestBody I18nColumn entity) {
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
    public IPage<I18nColumn> page(IPage<I18nColumn> page, I18nColumn req) {
        return service.page(page,req);
    }
}
