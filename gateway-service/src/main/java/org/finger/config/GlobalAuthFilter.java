package org.finger.config;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

import javax.crypto.SecretKey;
import java.util.Base64;
import java.util.List;

@Component
public class GlobalAuthFilter implements GlobalFilter, Ordered {

    // JWT密钥，从配置文件读取，格式为Base64编码
    @Value("${jwt.secret:mySecretKey}")
    private String jwtSecret;

    // 无需认证的公开路径列表（如登录、注册、健康检查等）
    private static final List<String> EXCLUDE_PATHS = List.of(
            "/login/",
            "/register/",
            "/public/",
            "/health",
            "/actuator/"
    );

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, org.springframework.cloud.gateway.filter.GatewayFilterChain chain) {

        String path = exchange.getRequest().getURI().getPath();

        // 第1步：检查是否是无需认证的路径，如果是则直接放行
        if (isExcludePath(path)) {
            return chain.filter(exchange);
        }

        // 第2步：从请求头中获取Authorization头（JWT Token）
        String authHeader = exchange.getRequest().getHeaders().getFirst(HttpHeaders.AUTHORIZATION);

        // 第3步：检查Authorization头是否存在且格式正确（应为 "Bearer TOKEN"）
        if (authHeader == null || !authHeader.startsWith("Bearer ")) {
            // Token缺失或格式错误，返回401未授权
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            exchange.getResponse().getHeaders().add("WWW-Authenticate", "Bearer");
            return exchange.getResponse().setComplete();
        }

        // 第4步：提取Token（去掉"Bearer "前缀）
        String token = authHeader.substring(7);

        try {
            // 第5步：验证JWT Token的有效性和签名
            Claims claims = validateToken(token);

            // 第6步：如果验证成功，将用户信息注入到请求头中传递给下游服务
            // 注意：必须使用 exchange.mutate() 来正确修改exchange对象
            ServerWebExchange newExchange = exchange.mutate().request(req -> req
                    .header("X-User-Id", claims.getSubject())           // 用户ID
                    .header("X-User-Name", claims.get("username", String.class))  // 用户名
                    .header("X-User-Roles", String.join(",", claims.get("roles", List.class)))  // 用户角色
            ).build();

            // 第7步：继续传递给下一个过滤器或后端服务
            return chain.filter(newExchange);

        } catch (Exception e) {
            // 验证失败（Token过期、签名错误等），返回401未授权
            exchange.getResponse().setStatusCode(HttpStatus.UNAUTHORIZED);
            return exchange.getResponse().setComplete();
        }
    }

    // 检查请求路径是否在无需认证的列表中
    private boolean isExcludePath(String path) {
        return EXCLUDE_PATHS.stream().anyMatch(path::startsWith);
    }

    // 验证JWT Token：检查签名和过期时间
    private Claims validateToken(String token) {
        // 使用Base64解码的密钥创建签名密钥
        SecretKey key = Keys.hmacShaKeyFor(Base64.getDecoder().decode(jwtSecret));

        // 解析JWT Token
        return Jwts.parserBuilder()
                .setSigningKey(key)      // 设置签名密钥
                .build()
                .parseClaimsJws(token)   // 解析并验证
                .getBody();              // 获取负载信息
    }

    @Override
    public int getOrder() {
        return -100;
    }
}
