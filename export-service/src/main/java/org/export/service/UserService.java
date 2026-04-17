package org.export.service;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import jakarta.annotation.Resource;
import org.export.entity.User;
import org.export.mapper.UserMapper;
import org.export.util.ExcelExportUtil;
import org.export.vo.UserExportVo;
import org.springframework.beans.BeanUtils;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

/**
 * 用户 service
 */
@Service
public class UserService {

    @Resource
    private UserMapper userMapper;

    @Resource
    private ExcelExportUtil excelExportUtil;

    /**
     * 根据语言-返回对应内容
     */
    public List<?> query(String lang) {
        List<User> userList= userMapper.selectList(new QueryWrapper<>());
        if (userList == null || userList.isEmpty()) {
            return null;
        }
        List<UserExportVo> resultList= userList.stream().map(user -> {
            UserExportVo vo = new UserExportVo();
            BeanUtils.copyProperties(user, vo);
            return vo;
        }).toList();
        return excelExportUtil.buildBody(resultList, UserExportVo.class, lang);
    }

    /**
     * 普通查询
     */
    public List<UserExportVo> query(){
        List<User> userList= userMapper.selectList(new QueryWrapper<>());
        return userList.stream().map(user -> {
            UserExportVo vo = new UserExportVo();
            BeanUtils.copyProperties(user, vo);
            return vo;
        }).collect(Collectors.toList());
    }

}
