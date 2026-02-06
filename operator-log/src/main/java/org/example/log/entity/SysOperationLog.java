package org.example.log.entity;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@TableName("t_sys_operation_log")
public class SysOperationLog {

    @TableId(type = IdType.AUTO)
    private Long id;

    private String moduleCode;
    private String moduleName;

    private String targetId;
    private String targetName;

    private String operateType;
    private String operateTypeName;

    private String beforeValue;
    private String afterValue;
    private String diffValue;

    private String remark;

    private String createdBy;

    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createdDate;

    /** 1 成功；0 失败 */
    private Integer status;

    private String errorMessage;
    /**  链路追踪ID */
    private String traceId;
}
