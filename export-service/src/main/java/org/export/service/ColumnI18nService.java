package org.export.service;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import jakarta.annotation.Resource;
import org.export.entity.I18nColumn;
import org.export.mapper.ColumnI18nMapper;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

@Service
public class ColumnI18nService {

    private final Map<String, String> cache = new ConcurrentHashMap<>();

    @Resource
    private ColumnI18nMapper mapper;

    public String get(String code, String lang) {
        String key = code + "_" + lang;
        return cache.computeIfAbsent(key, k -> {
            String val = mapper.getValue(code, lang);
            return val == null ? code : val;
        });
    }

    public void add(I18nColumn entity) {
        mapper.insert(entity);
    }

    public void update(I18nColumn entity) {
        mapper.updateById(entity);
    }

    public void delete(String id) {
        mapper.deleteById(id);
    }

    public IPage<I18nColumn> page(IPage<I18nColumn> page,I18nColumn req) {
        LambdaQueryWrapper<I18nColumn> wrapper= new LambdaQueryWrapper<>();
        wrapper.setEntity(req);
       return mapper.selectPage(page,wrapper);
    }
}