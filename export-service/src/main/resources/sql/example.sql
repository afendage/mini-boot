
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_i18n
-- ----------------------------
DROP TABLE IF EXISTS `t_i18n`;
CREATE TABLE `t_i18n`  (
                           `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键ID',
                           `code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '国际化key',
                           `lang` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '语言标识，如 zh_CN, en_US',
                           `value` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '翻译内容',
                           `remark` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL COMMENT '备注',
                           `create_time` datetime NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
                           `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
                           PRIMARY KEY (`id`) USING BTREE,
                           UNIQUE INDEX `uk_code_lang`(`code` ASC, `lang` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '国际化表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_i18n
-- ----------------------------
INSERT INTO `t_i18n` VALUES (1, 'user.login.button', 'zh_CN', '登录', NULL, '2026-03-30 20:58:57', '2026-03-30 20:58:57');
INSERT INTO `t_i18n` VALUES (2, 'user.login.button', 'en_US', 'Login', NULL, '2026-03-30 20:58:57', '2026-03-30 20:58:57');
INSERT INTO `t_i18n` VALUES (3, 'gender.M', 'zh_CN', '男', NULL, '2026-03-31 10:11:28', '2026-03-31 10:11:28');
INSERT INTO `t_i18n` VALUES (4, 'gender.M', 'en_US', 'Male', NULL, '2026-03-31 10:11:28', '2026-03-31 10:11:28');
INSERT INTO `t_i18n` VALUES (5, 'gender.F', 'zh_CN', '女', NULL, '2026-03-31 10:11:28', '2026-03-31 10:11:28');
INSERT INTO `t_i18n` VALUES (6, 'gender.F', 'en_US', 'Female', NULL, '2026-03-31 10:11:28', '2026-03-31 10:11:28');
INSERT INTO `t_i18n` VALUES (7, 'country.CN', 'zh_CN', '中国', NULL, '2026-03-31 10:21:33', '2026-03-31 10:21:33');
INSERT INTO `t_i18n` VALUES (8, 'country.CN', 'en_US', 'China', NULL, '2026-03-31 10:21:33', '2026-03-31 10:21:33');
INSERT INTO `t_i18n` VALUES (9, 'country.US', 'zh_CN', '美国', NULL, '2026-03-31 10:21:33', '2026-03-31 10:21:33');
INSERT INTO `t_i18n` VALUES (10, 'country.US', 'en_US', 'USA', NULL, '2026-03-31 10:21:33', '2026-03-31 10:21:33');
INSERT INTO `t_i18n` VALUES (11, 'country.JP', 'zh_CN', '日本', NULL, '2026-03-31 10:21:33', '2026-03-31 10:21:33');
INSERT INTO `t_i18n` VALUES (12, 'country.JP', 'en_US', 'Japan', NULL, '2026-03-31 10:21:33', '2026-03-31 10:21:33');
INSERT INTO `t_i18n` VALUES (13, 'user.status.0', 'zh_CN', '禁用', NULL, '2026-04-15 10:30:17', '2026-04-15 10:30:17');
INSERT INTO `t_i18n` VALUES (14, 'user.status.1', 'zh_CN', '启用', NULL, '2026-04-15 10:30:17', '2026-04-15 10:30:17');
INSERT INTO `t_i18n` VALUES (15, 'user.status.0', 'en_US', 'Disabled', NULL, '2026-04-15 10:30:17', '2026-04-15 10:30:17');
INSERT INTO `t_i18n` VALUES (16, 'user.status.1', 'en_US', 'Enabled', NULL, '2026-04-15 10:30:17', '2026-04-15 10:30:17');

-- ----------------------------
-- Table structure for t_i18n_column
-- ----------------------------
DROP TABLE IF EXISTS `t_i18n_column`;
CREATE TABLE `t_i18n_column`  (
                                  `id` bigint NOT NULL AUTO_INCREMENT,
                                  `code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
                                  `lang` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
                                  `value` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
                                  PRIMARY KEY (`id`) USING BTREE,
                                  UNIQUE INDEX `uk_code_lang`(`code` ASC, `lang` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_i18n_column
-- ----------------------------
INSERT INTO `t_i18n_column` VALUES (1, 'user.name', 'zh_CN', '用户名');
INSERT INTO `t_i18n_column` VALUES (2, 'user.gender', 'zh_CN', '性别');
INSERT INTO `t_i18n_column` VALUES (3, 'user.status', 'zh_CN', '状态');
INSERT INTO `t_i18n_column` VALUES (4, 'user.country', 'zh_CN', '国家');
INSERT INTO `t_i18n_column` VALUES (5, 'user.time', 'zh_CN', '时间');
INSERT INTO `t_i18n_column` VALUES (6, 'user.name', 'en_US', 'Name');
INSERT INTO `t_i18n_column` VALUES (7, 'user.gender', 'en_US', 'Gender');
INSERT INTO `t_i18n_column` VALUES (8, 'user.status', 'en_US', 'Status');
INSERT INTO `t_i18n_column` VALUES (9, 'user.country', 'en_US', 'Country');
INSERT INTO `t_i18n_column` VALUES (10, 'user.time', 'en_US', 'Time');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user`  (
                           `id` bigint NOT NULL AUTO_INCREMENT COMMENT '主键ID',
                           `name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '用户名',
                           `gender` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '性别：M/F',
                           `status` int NOT NULL COMMENT '状态：0禁用 1启用',
                           `country` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '国家：CN/US/JP',
                           `create_time` datetime NULL DEFAULT CURRENT_TIMESTAMP,
                           `update_time` datetime NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                           PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci COMMENT = '用户表' ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES (1, 'zhangsan', 'M', 1, 'CN', '2026-03-31 10:24:23', '2026-03-31 10:24:23');
INSERT INTO `t_user` VALUES (2, 'lisi', 'F', 0, 'US', '2026-03-31 10:24:23', '2026-03-31 10:24:23');
INSERT INTO `t_user` VALUES (3, 'wangwu', 'M', 1, 'JP', '2026-03-31 10:24:23', '2026-03-31 10:24:23');
INSERT INTO `t_user` VALUES (4, 'tom', 'M', 1, 'US', '2026-03-31 10:24:23', '2026-03-31 10:24:23');
INSERT INTO `t_user` VALUES (5, 'lucy', 'F', 0, 'CN', '2026-03-31 10:24:23', '2026-03-31 10:24:23');

SET FOREIGN_KEY_CHECKS = 1;

