package org.export.entity;

import lombok.Data;
import com.baomidou.mybatisplus.annotation.TableName;
import java.time.LocalDateTime;

/**
 * 用户表
 */
@Data
@TableName("t_user")
public class User {

    private Long id;

    private String name;

    private Integer status;

    private String gender;

    private String country;

    private LocalDateTime createTime;

    private LocalDateTime updateTime;
}