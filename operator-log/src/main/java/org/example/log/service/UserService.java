package org.example.log.service;

import lombok.RequiredArgsConstructor;
import org.example.log.annotation.OperationLog;
import org.example.log.entity.User;
import org.example.log.enums.OperateType;
import org.example.log.mapper.UserMapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserMapper userMapper;

    /**
     * 新增用户（INSERT）
     */
    @OperationLog(
            module = "USER",
            moduleName = "用户管理",
            type = OperateType.INSERT,
            typeName = "新增用户",
            entity = User.class
    )
    public Long createUser(String name, Integer age) {
        User user = new User();
        user.setName(name);
        user.setAge(age);
        user.setStatus(1);
        userMapper.insert(user);
        // 必须
        return user.getId();
    }

    /**
     * 更新用户（UPDATE + diff）
     */
    @OperationLog(
            module = "USER",
            moduleName = "用户管理",
            type = OperateType.UPDATE,
            typeName = "修改用户信息",
            entity = User.class,
            fieldNames = {
                    "name:姓名",
                    "age:年龄",
                    "status:状态"
            },
            id = "#id"
    )
    public void updateUser(Long id, String name, Integer age, Integer status) {
        User user = userMapper.selectById(id);
        user.setName(name);
        user.setAge(age);
        user.setStatus(status);
        userMapper.updateById(user);
    }

    /**
     * 删除用户（DELETE）
     */
    @OperationLog(
            module = "USER",
            moduleName = "用户管理",
            type = OperateType.DELETE,
            typeName = "删除用户",
            entity = User.class,
            id = "#id"
    )
    public void deleteUser(Long id) {
        userMapper.deleteById(id);
    }

    /**
     * 批量禁用用户（BATCH）
     */
    @OperationLog(
            module = "USER",
            moduleName = "用户管理",
            type = OperateType.BATCH,
            typeName = "批量禁用用户",
            condition = "#ids"
    )
    public int batchDisableUsers(List<Long> ids) {
        return 3;
    }

    /**
     * 批量删除用户（BATCH）
     */
    @OperationLog(
            module = "USER",
            moduleName = "用户管理",
            type = OperateType.BATCH,
            typeName = "批量删除无效用户",
            condition = "#ids"
    )
    public int batchDeleteInactiveUsers(List<Long> ids) {
//        return userMapper.deleteInactive();
        return 4;
    }
}

