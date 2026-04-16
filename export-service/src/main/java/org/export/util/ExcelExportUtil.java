package org.export.util;

import jakarta.annotation.Resource;
import lombok.val;
import org.export.annotation.ExcelColumn;
import org.export.annotation.ExcelDate;
import org.export.annotation.ExcelDict;
import org.export.annotation.ExcelEnum;
import org.export.service.ColumnI18nService;
import org.export.service.DictService;
import org.export.service.I18nService;
import org.springframework.stereotype.Component;

import java.lang.reflect.Field;
import java.text.SimpleDateFormat;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.*;

/**
 * 导出工具类
 */
@Component
public class ExcelExportUtil {

    @Resource
    private ColumnI18nService columnI18n;

    @Resource
    private DictService dict;

    @Resource
    private I18nService i18n;


    /**
     * 获取列头
     */
    private static <T> List<Field> getExcelFields(Class<T> clazz) {
        return Arrays.stream(clazz.getDeclaredFields()).filter(f -> f.isAnnotationPresent(ExcelColumn.class)).sorted(Comparator.comparing(Field::getName))
                .toList();
    }

    /**
     * 构建列头
     */
    public <T> List<List<String>> buildHead(Class<T> clazz, String lang) {
        List<Field> fields = getExcelFields(clazz);
        List<List<String>> head = new ArrayList<>();
        for (Field f : fields) {
            ExcelColumn col = f.getAnnotation(ExcelColumn.class);
            head.add(Collections.singletonList(columnI18n.get(col.value(), lang)));
        }
        return head;
    }

    /**
     * 构建导出数据
     */
    public <T> List<List<Object>> buildBody(List<T> data, Class<T> clazz, String lang) {
        List<Field> fields = getExcelFields(clazz);
        List<List<Object>> rows = new ArrayList<>();
        for (T obj : data) {
            List<Object> row = new ArrayList<>();
            for (Field f : fields) {
                f.setAccessible(true);
                Object val;
                try {
                    val = f.get(obj);
                    // 枚举
                    if (f.isAnnotationPresent(ExcelEnum.class) && val != null) {
                        val = i18n.get(f.getAnnotation(ExcelEnum.class).value() + val, lang);
                    }
                    // 日期
                    if (f.isAnnotationPresent(ExcelDate.class) && val != null) {
                        String pattern = f.getAnnotation(ExcelDate.class).value();
                        if (val instanceof Date date) {
                            val = new SimpleDateFormat(pattern).format(date);
                        } else if (val instanceof LocalDateTime ldt) {
                            val = ldt.format(DateTimeFormatter.ofPattern(pattern));
                        }
                    }
                    // 字典
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