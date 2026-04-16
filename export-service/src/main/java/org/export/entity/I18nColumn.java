package org.export.entity;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

/**
 * @author aengus
 * 表结构-转义字典表
 */
@Data
@TableName("t_i18n_column")
public class I18nColumn {

    private Long id;
    private String code;
    private String lang;
    private String value;

}