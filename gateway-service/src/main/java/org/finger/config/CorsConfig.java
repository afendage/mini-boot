package org.finger.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.cors.reactive.CorsWebFilter;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.reactive.UrlBasedCorsConfigurationSource;

import java.util.Arrays;
import java.util.List;

/**
 * CORS（跨域资源共享）配置类
 * 
 * 功能说明：
 * 1. 解决浏览器同源策略导致的跨域访问问题
 * 2. 支持配置化的CORS策略，便于不同环境管理
 * 3. 提供灵活的源、方法、头部配置
 * 4. 暴露自定义响应头供前端使用
 * 
 * 配置项说明：
 * - cors.allowed-origins: 允许的源地址（默认：*，表示所有源）
 * - cors.allowed-methods: 允许的HTTP方法（默认：*，表示所有方法）
 * - cors.allowed-headers: 允许的请求头（默认：*，表示所有头部）
 * - cors.allow-credentials: 是否允许携带凭证（默认：false）
 * - cors.max-age: 预检请求缓存时间（默认：3600秒）
 * 
 * @Configuration 标识这是一个Spring配置类
 */
@Configuration
public class CorsConfig {

    /** 允许的源地址，支持逗号分隔的多个地址，*表示所有源 */
    @Value("${cors.allowed-origins:*}")
    private String allowedOrigins;

    /** 允许的HTTP方法，支持逗号分隔，*表示所有方法 */
    @Value("${cors.allowed-methods:*}")
    private String allowedMethods;

    /** 允许的请求头，支持逗号分隔，*表示所有头部 */
    @Value("${cors.allowed-headers:*}")
    private String allowedHeaders;

    /** 是否允许携带凭证（如Cookie、Authorization头等） */
    @Value("${cors.allow-credentials:false}")
    private boolean allowCredentials;

    /** 预检请求（OPTIONS）的缓存时间，单位：秒 */
    @Value("${cors.max-age:3600}")
    private long maxAge;

    /**
     * 创建CORS Web过滤器Bean
     * 
     * 配置策略：
     * 1. 支持通配符(*)和具体地址的混合配置
     * 2. 自动解析逗号分隔的配置项
     * 3. 暴露自定义响应头供前端使用
     * 4. 应用到所有路径（/**）
     * 
     * @return 配置好的CorsWebFilter实例
     */
    @Bean
    public CorsWebFilter corsWebFilter() {
        // 创建CORS配置对象
        CorsConfiguration config = new CorsConfiguration();

        // 1. 配置允许的源地址
        if ("*".equals(allowedOrigins)) {
            // 允许所有源：注意，这种配置在生产环境不安全
            config.addAllowedOrigin("*");
        } else {
            // 解析逗号分隔的源地址列表，去除空格
            List<String> origins = Arrays.asList(allowedOrigins.split(","));
            origins.stream()
                    .map(String::trim)
                    .forEach(config::addAllowedOrigin);
        }

        // 2. 配置允许的HTTP方法
        if ("*".equals(allowedMethods)) {
            config.addAllowedMethod("*");
        } else {
            List<String> methods = Arrays.asList(allowedMethods.split(","));
            methods.stream()
                    .map(String::trim)
                    .forEach(config::addAllowedMethod);
        }

        // 3. 配置允许的请求头
        if ("*".equals(allowedHeaders)) {
            config.addAllowedHeader("*");
        } else {
            List<String> headers = Arrays.asList(allowedHeaders.split(","));
            headers.stream()
                    .map(String::trim)
                    .forEach(config::addAllowedHeader);
        }

        // 4. 配置暴露给前端的响应头（前端JavaScript可以访问这些头）
        config.setExposedHeaders(Arrays.asList(
            "X-Total-Count",    // 总记录数（分页用）
            "X-Page-Count",     // 总页数（分页用）
            "X-Trace-Id"        // 追踪ID（链路追踪用）
        ));

        // 5. 是否允许请求携带凭证（Cookie、Authorization等）
        // 注意：当设置为true时，allowedOrigins不能为*
        config.setAllowCredentials(allowCredentials);

        // 6. 预检请求（OPTIONS）的缓存时间，单位秒（减少浏览器预检请求频率）
        config.setMaxAge(maxAge);

        // 7. 创建URL基础的CORS配置源，应用到所有路径
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", config);

        // 8. 返回CORS Web过滤器
        return new CorsWebFilter(source);
    }
}
