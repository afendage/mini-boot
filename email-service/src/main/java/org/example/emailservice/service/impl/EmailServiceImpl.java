package org.example.emailservice.service.impl;

import jakarta.annotation.Resource;
import lombok.RequiredArgsConstructor;
import org.example.emailservice.service.EmailService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class EmailServiceImpl implements EmailService {

    @Resource
    private JavaMailSender mailSender;

    @Value("${spring.mail.username}")
    private String fromEmail;  // 发件人邮箱

    @Value("${app.verify-code.email-template}")
    private String emailTemplate;  // 邮件模板

    @Override
    public void sendVerifyCodeEmail(String to, String code, int expireMinutes) {
        SimpleMailMessage message = new SimpleMailMessage();
        message.setFrom(fromEmail);
        message.setTo(to);
        message.setSubject("注册验证码");
        message.setText(String.format(emailTemplate, code, expireMinutes));
        mailSender.send(message);  // 发送邮件（实际生产需异步处理，避免阻塞）
    }
}
