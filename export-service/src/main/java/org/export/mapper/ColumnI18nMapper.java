package org.export.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

@Mapper
public interface ColumnI18nMapper {

    @Select("select value from t_i18n_column where code=#{code} and lang=#{lang}")
    String getValue(@Param("code") String code, @Param("lang") String lang);
}
