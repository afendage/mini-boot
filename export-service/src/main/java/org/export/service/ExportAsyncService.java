package org.export.service;

import com.alibaba.excel.EasyExcel;
import com.alibaba.excel.ExcelWriter;
import com.alibaba.excel.write.metadata.WriteSheet;
import jakarta.annotation.Resource;
import org.export.limiter.ExportLimiter;
import org.export.util.AutoWidthStrategy;
import org.export.util.ExcelExportUtil;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.function.Function;
import java.util.function.Supplier;

@Service
public class ExportAsyncService {

    @Resource
    private ExcelExportUtil excelExportUtil;
    @Resource
    private ExportLimiter limiter;

    /**
     * 分页导出
     */
    @Async
    public <T> void export(Long taskId, Function<Integer, List<T>> pageQuery, Class<T> clazz, String lang) {
        try {
            ExcelWriter writer = EasyExcel.write("export_" + taskId + ".xlsx").registerWriteHandler(new AutoWidthStrategy()).build();
            WriteSheet sheet = EasyExcel.writerSheet("sheet").head(excelExportUtil.buildHead(clazz, lang)).build();
            int page = 1;
            while (true) {
                List<T> list = pageQuery.apply(page);
                if (list.isEmpty()) {
                    break;
                }
                writer.write(excelExportUtil.buildBody(list, clazz, lang), sheet);
                page++;
            }
            writer.finish();
        } finally {
            limiter.releaseGlobal();
        }
    }

    /**
     * 一次性导出
     */
    @Async
    public <T> void exportAll(Long taskId, Supplier<List<T>> fullQuery, Class<T> clazz, String lang) {
        try {
            ExcelWriter writer = EasyExcel.write("export_" + taskId + ".xlsx").registerWriteHandler(new AutoWidthStrategy()).build();
            WriteSheet sheet = EasyExcel.writerSheet("sheet").head(excelExportUtil.buildHead(clazz, lang)).build();
            List<T> list = fullQuery.get();
            if (list != null && !list.isEmpty()) {
                writer.write(excelExportUtil.buildBody(list, clazz, lang), sheet);
            }
            writer.finish();
        } finally {
            limiter.releaseGlobal();
        }
    }
}
