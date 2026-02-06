package org.example.config;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.util.Date;

@Component
public class JwtUtils {
    @Value("${jwt.secret}")
    private String secret;
    @Value("${jwt.expiration}")
    private long expiration;

    // 生成 JWT 令牌
    public String generateToken(String username) {
        Date now = new Date();
        Date expirationDate = new Date(now.getTime() + expiration);

        return Jwts.builder()
                .setSubject(username)  // 主题（存储用户名）
                .setIssuedAt(now)      // 签发时间
                .setExpiration(expirationDate)  // 过期时间
                .signWith(SignatureAlgorithm.HS512, secret)  // 签名算法 + 密钥
                .compact();
    }

    // 从令牌中获取用户名
    public String getUsernameFromToken(String token) {
        return Jwts.parserBuilder()
                .setSigningKey(secret)
                .build()
                .parseClaimsJws(token)
                .getBody()
                .getSubject();
    }

    // 验证令牌是否有效（未过期且签名正确）
    public boolean validateToken(String token) {
        try {
            Jwts.parserBuilder().setSigningKey(secret).build().parseClaimsJws(token);
            return true;
        } catch (Exception e) {
            return false; // 令牌无效（过期、签名错误等）
        }
    }

    @Value("${jwt.token-header:Authorization}")
    private String tokenHeader;

    @Value("${jwt.token-prefix:Bearer}")
    private String tokenPrefix;

    public String getTokenHeader() {
        return tokenHeader;
    }

    public String getTokenPrefix() {
        return tokenPrefix;
    }

}

