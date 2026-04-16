package org.export.service;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import jakarta.annotation.Resource;
import org.export.entity.I18n;
import org.export.entity.I18nColumn;
import org.export.mapper.I18nMapper;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class I18nService {

    private final Map<String, String> cache = new ConcurrentHashMap<>();

    @Resource
    private I18nMapper mapper;

    public String get(String code, String lang) {
        String key = code + "_" + lang;
        return cache.computeIfAbsent(key, k -> {
            String val = mapper.getValue(code, lang);
            return val == null ? code : val;
        });
    }

    public void add(I18n entity) {
        mapper.insert(entity);
    }

    public void update(I18n entity) {
        mapper.updateById(entity);
    }

    public void delete(String id) {
        mapper.deleteById(id);
    }

    public IPage<I18n> page(IPage<I18n> page, I18n req) {
        LambdaQueryWrapper<I18n> wrapper= new LambdaQueryWrapper<>();
        wrapper.setEntity(req);
        return mapper.selectPage(page,wrapper);
    }
}
