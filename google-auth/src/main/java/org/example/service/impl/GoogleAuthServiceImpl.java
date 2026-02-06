package org.example.service.impl;

import com.warrenstrange.googleauth.GoogleAuthenticatorConfig;
import org.example.service.GoogleAuthService;
import com.warrenstrange.googleauth.GoogleAuthenticator;
import com.warrenstrange.googleauth.GoogleAuthenticatorKey;
import org.springframework.stereotype.Service;

import java.util.concurrent.TimeUnit;

@Service
public class GoogleAuthServiceImpl implements GoogleAuthService {

    private final GoogleAuthenticatorConfig config = new GoogleAuthenticatorConfig.GoogleAuthenticatorConfigBuilder()
            .setWindowSize(1)
            .setTimeStepSizeInMillis(TimeUnit.SECONDS.toMillis(30))
            .build();

    private final GoogleAuthenticator gAuth = new GoogleAuthenticator(config);


    /**
     * 验证用户输入的谷歌验证码
     * @param secretKey 用户绑定的密钥（从数据库查询）
     * @param code 用户输入的 6 位验证码
     * @return true=验证通过，false=验证失败
     */
    @Override
    public boolean verifyCode(String secretKey, int code) {
        // 注意：code 需为整数（用户输入的字符串需转换为 int）
        // 验证逻辑：默认允许 ±1 个时间窗口（每个窗口 30 秒），避免用户输入延迟导致验证失败
        return gAuth.authorize(secretKey, code);
    }


    /**
     * 生成密钥与二维码 URL（供前端展示）
     * @param username 用户唯一标识（如用户名/邮箱）
     * @param issuer 应用名称（如 "MyApp"）
     * @return 包含密钥和二维码 URL 的对象
     */
    @Override
    public GoogleAuthResult generateKey(String username, String issuer) {
        // 1. 生成随机密钥（默认 160 位，符合 TOTP 标准）
        GoogleAuthenticatorKey key = gAuth.createCredentials();
        String secretKey = key.getKey(); // 用户密钥（需持久化存储，与用户绑定）

        // 2. 生成二维码内容（OTP URI 格式）
        String otpUri = String.format(
                "otpauth://totp/%s:%s?secret=%s&issuer=%s",
                issuer, username, secretKey, issuer
        );

        // 3. 生成二维码图片 URL（可选：使用第三方 API 或本地生成）
        // 示例：使用 Google Charts API 生成二维码（生产环境建议本地生成，避免依赖外部服务）
        /*String qrCodeUrl = "https://chart.googleapis.com/chart?" +
                "chs=200x200&" + // 尺寸
                "chld=M|0&" +    // 纠错级别
                "cht=qr&" +      // 类型为二维码
                "chl=" + otpUri;*/ // 二维码内容（OTP URI）

        return new GoogleAuthResult(secretKey, otpUri);
    }

    // 内部类：封装密钥和二维码 URL
    public static class GoogleAuthResult {
        private final String secretKey;
        private final String qrCodeUrl;

        public GoogleAuthResult(String secretKey, String qrCodeUrl) {
            this.secretKey = secretKey;
            this.qrCodeUrl = qrCodeUrl;
        }

        // Getter
        public String getSecretKey() { return secretKey; }
        public String getQrCodeUrl() { return qrCodeUrl; }
    }
}

