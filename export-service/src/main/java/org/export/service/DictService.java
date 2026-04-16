package org.export.service;

import jakarta.annotation.Resource;
import org.export.mapper.I18nMapper;
import org.springframework.stereotype.Service;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

/**
 * 字典转义 service
 */
@Service
public class DictService {

    private final Map<String, String> cache = new ConcurrentHashMap<>();

    @Resource
    private I18nMapper i18nMapper;

    public String get(String dict, String code, String lang) {
        String fullCode = dict + "." + code;
        String key = fullCode + ":" + lang;
        return cache.computeIfAbsent(key, k -> {
            String val = i18nMapper.getValue(fullCode, lang);
            return val == null ? code : val;
        });
    }
}
