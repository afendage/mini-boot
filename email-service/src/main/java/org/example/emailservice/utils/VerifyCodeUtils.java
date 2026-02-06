package org.example.emailservice.utils;

import cn.hutool.core.util.RandomUtil;

/**
 * 验证码生成工具类
 */
public class VerifyCodeUtils {

    /**
     * 生成指定长度的数字验证码
     */
    public static String generateNumericCode(int length) {
        return RandomUtil.randomNumbers(length);
    }
}
