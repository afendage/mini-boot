package org.example.emailservice.service;

/**
 * 邮箱发送服务接口
 */
public interface EmailService {

    /**
     * 发送验证码邮件
     * @param to 收件人邮箱
     * @param code 验证码
     * @param expireMinutes 有效期（分钟）
     */
    void sendVerifyCodeEmail(String to, String code, int expireMinutes);
}

