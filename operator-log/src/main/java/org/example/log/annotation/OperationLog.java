package org.example.log.annotation;

import org.example.log.enums.OperateType;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * @author aengus
 */
@Target(ElementType.METHOD)
@Retention(RetentionPolicy.RUNTIME)
public @interface OperationLog {

    /** 模块编码 */
    String module();

    /** 模块名称 */
    String moduleName();

    /** 操作类型（create / update / delete） */
    OperateType type();

    /** 操作类型名称（创建 / 修改 / 删除） */
    String typeName();

    /** 指定数据库实体类（用于查询 beforeObj） */
    Class<?> entity() default Void.class;

    /** 通过 SpEL 从方法参数中提取主键（如 #bo.id） */
    String id() default "";

    String targetId() default "";

    String targetName() default "";

    /** 指定 diff 字段映射 例如 {"name:名称","status:状态"} */
    String[] fieldNames() default {};

    /** 额外备注 */
    String remark() default "";

    /** ⭐ 批量操作条件描述 */
    String condition() default "";

}

