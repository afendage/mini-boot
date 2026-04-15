package org.export.vo;

import lombok.Data;
import org.export.annotation.ExcelColumn;
import org.export.annotation.ExcelDate;
import org.export.annotation.ExcelDict;
import org.export.annotation.ExcelEnum;
import java.time.LocalDateTime;

@Data
public class UserExportVo {

    @ExcelColumn("user.name")
    private String name;

    @ExcelColumn("user.gender")
    @ExcelDict(dict = "gender")
    private String gender;

    @ExcelColumn("user.status")
    @ExcelEnum("user.status.")
    private Integer status;

    @ExcelColumn("user.country")
    @ExcelDict(dict = "country")
    private String country;

    @ExcelColumn("user.time")
    @ExcelDate("yyyy-MM-dd HH:mm:ss")
    private LocalDateTime createTime;
}