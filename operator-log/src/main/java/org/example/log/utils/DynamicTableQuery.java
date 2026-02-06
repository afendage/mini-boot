package org.example.log.utils;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

import java.sql.*;
import java.util.HashMap;
import java.util.Map;

public class DynamicTableQuery {

    private final SqlSessionFactory sqlSessionFactory;

    public DynamicTableQuery(SqlSessionFactory sqlSessionFactory) {
        this.sqlSessionFactory = sqlSessionFactory;
    }

    public Map<String, Object> queryOne(String tableName, String keyColumn, Object keyValue)
            throws SQLException {

        String sql = "SELECT * FROM " + safeName(tableName)
                + " WHERE " + safeName(keyColumn) + " = ? LIMIT 1";

        try (SqlSession session = sqlSessionFactory.openSession();
             Connection conn = session.getConnection();
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setObject(1, keyValue);

            try (ResultSet rs = ps.executeQuery()) {
                if (!rs.next()) {
                    return null;
                }

                ResultSetMetaData meta = rs.getMetaData();
                int count = meta.getColumnCount();
                Map<String, Object> map = new HashMap<>(count);

                for (int i = 1; i <= count; i++) {
                    map.put(meta.getColumnLabel(i), rs.getObject(i));
                }

                return map;
            }
        }
    }

    /**
     * 防止 SQL 注入，只允许字母、数字、下划线
     */
    private String safeName(String name) {
        if (!name.matches("[a-zA-Z0-9_]+")) {
            throw new IllegalArgumentException("Invalid table or column name: " + name);
        }
        return name;
    }
}

