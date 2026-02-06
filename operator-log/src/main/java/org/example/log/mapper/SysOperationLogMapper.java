package org.example.log.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;
import org.example.log.entity.SysOperationLog;

@Mapper
public interface SysOperationLogMapper extends BaseMapper<SysOperationLog> {
}

