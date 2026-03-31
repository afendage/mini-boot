CREATE TABLE t_i18n (
                        id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
                        code VARCHAR(255) NOT NULL COMMENT '国际化key',
                        lang VARCHAR(20) NOT NULL COMMENT '语言标识，如 zh_CN, en_US',
                        value TEXT NOT NULL COMMENT '翻译内容',
                        remark VARCHAR(255) DEFAULT NULL COMMENT '备注',
                        create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
                        update_time DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',

                        UNIQUE KEY uk_code_lang (code, lang)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='国际化表';

INSERT INTO t_i18n (code, lang, value)
VALUES
    ('user.login.button', 'zh_CN', '登录'),
    ('user.login.button', 'en_US', 'Login');