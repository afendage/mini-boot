package org.export.service;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.export.entity.User;
import org.export.mapper.UserMapper;
import org.export.vo.UserExportVo;
import org.springframework.beans.BeanUtils;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class UserService {

    @Resource
    private UserMapper userMapper;

    public List<UserExportVo> query(){
        List<User> userList= userMapper.selectList(new QueryWrapper<>());
        return userList.stream().map(user -> {
            UserExportVo vo = new UserExportVo();
            BeanUtils.copyProperties(user, vo);
            return vo;
        }).collect(Collectors.toList());
    }

}
