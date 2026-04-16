package org.export.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
import org.export.entity.I18nColumn;

@Mapper
public interface ColumnI18nMapper extends BaseMapper<I18nColumn> {

    @Select("select value from t_i18n_column where code=#{code} and lang=#{lang}")
    String getValue(@Param("code") String code, @Param("lang") String lang);
}
