package org.export.util;

import com.alibaba.excel.metadata.Head;
import com.alibaba.excel.metadata.data.WriteCellData;
import com.alibaba.excel.write.metadata.holder.WriteSheetHolder;
import com.alibaba.excel.write.style.column.AbstractColumnWidthStyleStrategy;
import org.apache.poi.ss.usermodel.Cell;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 自动设置列宽度
 */
public class AutoWidthStrategy extends AbstractColumnWidthStyleStrategy {

    private static final int MAX_COLUMN_WIDTH = 50;
    private final Map<Integer, Integer> cache = new HashMap<>();

    @Override
    protected void setColumnWidth(WriteSheetHolder writeSheetHolder, List<WriteCellData<?>> cellDataList, Cell cell, Head head, Integer columnIndex, Boolean isHead) {

        int length = 0;

        if (Boolean.TRUE.equals(isHead)) {
            String headValue = cell.getStringCellValue();
            length = headValue == null ? 0 : headValue.length();
        } else if (cellDataList != null && !cellDataList.isEmpty()) {
            String value = cellDataList.get(0).getStringValue();
            length = value == null ? 0 : value.length();
        }

        length = Math.min(length, MAX_COLUMN_WIDTH);

        Integer max = cache.get(columnIndex);
        if (max == null || length > max) {
            cache.put(columnIndex, length);
            writeSheetHolder.getSheet().setColumnWidth(columnIndex, length * 256);
        }
    }
}
