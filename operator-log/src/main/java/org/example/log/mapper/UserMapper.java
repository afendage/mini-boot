package org.example.log.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.example.log.entity.User;

import java.util.List;

@Mapper
public interface UserMapper extends BaseMapper<User> {

    /**
     * 批量禁用用户
     */
    int disableByIds(@Param("ids") List<Long> ids);

    /**
     * 批量删除无效用户
     */
    int deleteInactive();
}

