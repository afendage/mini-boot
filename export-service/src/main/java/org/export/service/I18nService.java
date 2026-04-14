package org.export.service;

import jakarta.annotation.Resource;
import org.export.mapper.I18nMapper;
import org.springframework.stereotype.Service;

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
}
