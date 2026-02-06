package org.example.emailservice.service;

/**
 * 验证码服务接口（发送+验证）
 */
public interface EmailVerifyCodeService {

    /**
     * 发送邮箱验证码（带防刷限制）
     * @param email 目标邮箱
     * @param ip 发送者IP（用于防刷）
     * @throws Exception 发送失败或频率限制时抛出异常
     */
    void sendEmailVerifyCode(String email, String ip) throws Exception;

    /**
     * 验证邮箱验证码
     * @param email 邮箱
     * @param code 用户输入的验证码
     * @return true：验证通过；false：验证失败
     */
    boolean validateEmailVerifyCode(String email, String code);
}

