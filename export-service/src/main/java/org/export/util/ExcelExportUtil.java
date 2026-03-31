package org.export.util;

import org.export.annotation.ExcelColumn;
import org.export.annotation.ExcelDate;
import org.export.annotation.ExcelDict;
import org.export.annotation.ExcelEnum;
import org.export.service.DictService;
import org.export.service.I18nService;

import java.lang.reflect.Field;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ExcelExportUtil {

    public static <T> List<List<String>> buildHead(Class<T> clazz, String lang) {
        I18nService i18n = SpringContext.getBean(I18nService.class);
        List<List<String>> head = new ArrayList<>();
        for (Field f : clazz.getDeclaredFields()) {
            ExcelColumn col = f.getAnnotation(ExcelColumn.class);
            if (col != null) {
                head.add(Collections.singletonList(i18n.get(col.value(), lang)));
            }
        }
        return head;
    }

    public static <T> List<List<Object>> buildBody(List<T> data, Class<T> clazz, String lang) {
        I18nService i18n = SpringContext.getBean(I18nService.class);
        DictService dict = SpringContext.getBean(DictService.class);
        List<List<Object>> rows = new ArrayList<>();
        for (T obj : data) {
            List<Object> row = new ArrayList<>();
            for (Field f : clazz.getDeclaredFields()) {
                f.setAccessible(true);
                Object val;
                try {
                    val = f.get(obj);
                    if (f.isAnnotationPresent(ExcelEnum.class) && val != null) {
                        val = i18n.get(f.getAnnotation(ExcelEnum.class).value() + val, lang);
                    }
                    if (f.isAnnotationPresent(ExcelDate.class) && val != null) {
                        val = new SimpleDateFormat(f.getAnnotation(ExcelDate.class).value()).format(val);
                    }
                    if (f.isAnnotationPresent(ExcelDict.class) && val != null) {
                        val = dict.get(f.getAnnotation(ExcelDict.class).dict(), val.toString(), lang);
                    }
                } catch (Exception e) {
                    val = "";
                }
                row.add(val);
            }
            rows.add(row);
        }
        return rows;
    }
}