package org.example.log.utils;

import com.alibaba.fastjson2.JSON;

import java.util.*;

public class DiffUtils {

    public static Map<String, Map<String, Object>> diff(
            Object oldObj,
            Object newObj,
            Map<String, String> fieldNameMap) {

        Map<String, Map<String, Object>> diffMap = new LinkedHashMap<>();

        if (oldObj == null && newObj == null) {
            return diffMap;
        }

        // 转成 Map（深拷贝）
        Map<String, Object> oldMap =
                JSON.parseObject(JSON.toJSONString(oldObj), Map.class);
        Map<String, Object> newMap =
                JSON.parseObject(JSON.toJSONString(newObj), Map.class);

        // 遍历所有字段
        for (String key : newMap.keySet()) {

            Object before = oldMap.get(key);
            Object after = newMap.get(key);

            // 值相同，不记录
            if (Objects.equals(before, after)) {
                continue;
            }

            String name = fieldNameMap.getOrDefault(key, key);

            Map<String, Object> change = new HashMap<>();
            change.put("field", name);
            change.put("before", before);
            change.put("after", after);

            diffMap.put(key, change);
        }

        return diffMap;
    }

    // 默认忽略的字段
    private static final Set<String> IGNORE_FIELDS = Set.of(
            "updatedAt",
            "updateTime",
            "createTime",
            "version"
    );

    /**
     * ② 自动 diff（新增）
     */
    public static Map<String, Map<String, Object>> diffAuto(
            Object oldObj,
            Object newObj) {

        Map<String, Map<String, Object>> diffMap = new LinkedHashMap<>();

        Map<String, Object> oldMap = toMap(oldObj);
        Map<String, Object> newMap = toMap(newObj);

        for (String key : newMap.keySet()) {

            if (IGNORE_FIELDS.contains(key)) {
                continue;
            }

            Object before = oldMap.get(key);
            Object after = newMap.get(key);

            if (Objects.equals(before, after)) {
                continue;
            }

            Map<String, Object> change = new HashMap<>();
            change.put("field", key);
            change.put("before", before);
            change.put("after", after);

            diffMap.put(key, change);
        }

        return diffMap;
    }

    private static Map<String, Object> toMap(Object obj) {
        return JSON.parseObject(JSON.toJSONString(obj), Map.class);
    }
}

