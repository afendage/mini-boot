package org.export.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import java.time.LocalDateTime;

/**
 * @author aengus
 */
@Data
@TableName("t_i18n")
public class I18n {

    private Long id;
    private String code;
    private String lang;
    private String value;
    private String remark;
    private LocalDateTime createTime;
    private LocalDateTime updateTime;

}