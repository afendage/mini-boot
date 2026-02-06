package org.example.emailservice.service.impl;

import cn.hutool.core.util.StrUtil;
import lombok.RequiredArgsConstructor;
import org.example.emailservice.service.EmailService;
import org.example.emailservice.service.EmailVerifyCodeService;
import org.example.emailservice.utils.VerifyCodeUtils;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;

import java.util.concurrent.TimeUnit;

@Service
@RequiredArgsConstructor
public class EmailVerifyCodeServiceImpl implements EmailVerifyCodeService {

    private final StringRedisTemplate redisTemplate;
    private final EmailService emailService;

    // 配置参数（从application.yml注入）
    @Value("${app.verify-code.length}")
    private int codeLength;
    @Value("${app.verify-code.expire-seconds}")
    private int expireSeconds;
    @Value("${app.verify-code.send-interval-seconds}")
    private int sendIntervalSeconds;

    // Redis Key前缀（避免Key冲突）
    private static final String CODE_KEY_PREFIX = "verify:email:code:";       // 验证码存储Key
    private static final String INTERVAL_KEY_PREFIX = "verify:email:interval:"; // 发送间隔限制Key

    @Override
    public void sendEmailVerifyCode(String email, String ip) throws Exception {
        // 1. 参数校验
        if (StrUtil.isBlank(email) || !email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$")) {
            throw new IllegalArgumentException("邮箱格式不正确");
        }

        // 2. 防刷限制：同一邮箱/IP在间隔时间内不允许重复发送
        String intervalKey = INTERVAL_KEY_PREFIX + email + ":" + ip;
        Boolean hasSent = redisTemplate.hasKey(intervalKey);
        if (Boolean.TRUE.equals(hasSent)) {
            throw new RuntimeException("发送频率过高，请稍后再试");
        }

        // 3. 生成验证码
        String code = VerifyCodeUtils.generateNumericCode(codeLength);

        // 4. 存储验证码到Redis（带过期时间）
        String codeKey = CODE_KEY_PREFIX + email;
        redisTemplate.opsForValue().set(codeKey, code, expireSeconds, TimeUnit.SECONDS);

        // 5. 设置发送间隔限制
        redisTemplate.opsForValue().set(intervalKey, "1", sendIntervalSeconds, TimeUnit.SECONDS);

        // 6. 发送邮件（实际生产建议用@Async异步发送，避免阻塞）
        emailService.sendVerifyCodeEmail(email, code, expireSeconds / 60);
    }

    @Override
    public boolean validateEmailVerifyCode(String email, String code) {
        // 1. 参数校验
        if (StrUtil.isBlank(email) || StrUtil.isBlank(code)) {
            return false;
        }

        // 2. 从Redis获取存储的验证码
        String codeKey = CODE_KEY_PREFIX + email;
        String storedCode = redisTemplate.opsForValue().get(codeKey);

        // 3. 校验验证码（非空+匹配+未过期）
        if (StrUtil.equals(code, storedCode)) {
            redisTemplate.delete(codeKey); // 验证通过后删除，防止重复使用
            return true;
        }
        return false;
    }
}

