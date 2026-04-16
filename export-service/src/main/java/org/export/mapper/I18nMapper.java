package org.export.mapper;


import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.export.entity.I18n;

@Mapper
public interface I18nMapper extends BaseMapper<I18n> {

    @Select("select value from t_i18n where code=#{code} and lang=#{lang}")
    String getValue(@Param("code") String code, @Param("lang") String lang);
}
