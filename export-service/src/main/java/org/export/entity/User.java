package org.export.entity;

import lombok.Data;
import com.baomidou.mybatisplus.annotation.TableName;
import java.time.LocalDateTime;

@Data
@TableName("t_user")
public class User {

    private Long id;

    private String name;

    private Integer age;

    private Integer status;

    private LocalDateTime createTime;

    private LocalDateTime updateTime;
}