package org.finger.config;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.core.Ordered;
import org.springframework.http.HttpHeaders;
import org.springframework.http.server.reactive.ServerHttpRequest;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.UUID;

/**
 * 全局日志过滤器
 * 
 * 功能说明：
 * 1. 为每个请求生成唯一的追踪ID，用于链路追踪
 * 2. 记录请求开始、完成和失败的详细日志
 * 3. 计算请求处理时间（性能监控）
 * 4. 提取客户端真实IP地址
 * 5. 记录User-Agent等关键请求信息
 * 
 * 实现原理：
 * - 使用Spring Cloud Gateway的GlobalFilter接口
 * - 通过MDC（Mapped Diagnostic Context）传递追踪ID
 * - 使用Reactor的响应式编程模型处理异步请求
 * 
 * @Component 将该类注册为Spring组件
 */
@Component
public class LogFilter implements GlobalFilter, Ordered {

    /** 日志记录器 */
    private static final Logger logger = LoggerFactory.getLogger(LogFilter.class);
    
    /** 时间格式化器，用于日志时间戳 */
    private static final DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss.SSS");

    /**
     * 过滤器的核心处理方法
     * 
     * 处理流程：
     * 1. 生成唯一的追踪ID并设置到MDC
     * 2. 提取请求的关键信息（方法、URI、IP、User-Agent等）
     * 3. 记录请求开始的详细日志
     * 4. 执行后续过滤器链
     * 5. 根据执行结果记录完成或失败的日志
     * 6. 清理MDC中的追踪ID
     * 
     * @param exchange 服务器Web交换对象，包含请求和响应信息
     * @param chain 过滤器链，用于执行后续过滤器
     * @return Mono<Void> 异步处理完成信号
     */
    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {

        // 1. 记录请求开始时间，用于计算处理时长
        long startTime = System.currentTimeMillis();
        
        // 2. 生成唯一的追踪ID（去除UUID中的横线，便于日志阅读）
        String traceId = UUID.randomUUID().toString().replace("-", "");
        
        // 3. 将追踪ID设置到MDC，这样在同一线程中的所有日志都会包含这个ID
        MDC.put("traceId", traceId);
        
        // 4. 提取请求的关键信息
        ServerHttpRequest request = exchange.getRequest();
        String method = request.getMethod().name(); // HTTP方法（GET、POST等）
        String uri = request.getURI().toString(); // 请求URI
        String clientIp = getClientIp(request); // 客户端真实IP
        String userAgent = request.getHeaders().getFirst(HttpHeaders.USER_AGENT); // 用户代理
        
        // 5. 记录请求开始的详细日志
        logger.info("Request Started - TraceId: {}, Time: {}, Method: {}, URI: {}, ClientIP: {}, UserAgent: {}", 
                traceId, 
                LocalDateTime.now().format(formatter), 
                method, 
                uri, 
                clientIp, 
                userAgent);

        // 6. 执行过滤器链，并在成功和失败时分别记录日志
        return chain.filter(exchange)
                .doOnSuccess(aVoid -> {
                    // 请求成功完成时的处理
                    long endTime = System.currentTimeMillis();
                    long duration = endTime - startTime; // 计算请求处理时长
                    
                    // 获取响应状态码（防止空指针异常）
                    int statusCode = exchange.getResponse().getStatusCode() != null ? 
                            exchange.getResponse().getStatusCode().value() : 0;
                    
                    // 记录请求完成的详细日志
                    logger.info("Request Completed - TraceId: {}, Time: {}, Duration: {}ms, StatusCode: {}, Method: {}, URI: {}", 
                            traceId, 
                            LocalDateTime.now().format(formatter), 
                            duration, 
                            statusCode, 
                            method, 
                            uri);
                    
                    // 清理MDC中的追踪ID
                    MDC.remove("traceId");
                })
                .doOnError(throwable -> {
                    // 请求失败时的处理
                    long endTime = System.currentTimeMillis();
                    long duration = endTime - startTime; // 计算请求处理时长
                    
                    // 记录请求失败的详细日志，包含异常信息
                    logger.error("Request Failed - TraceId: {}, Time: {}, Duration: {}ms, Method: {}, URI: {}, Error: {}", 
                            traceId, 
                            LocalDateTime.now().format(formatter), 
                            duration, 
                            method, 
                            uri, 
                            throwable.getMessage(), 
                            throwable);
                    
                    // 清理MDC中的追踪ID
                    MDC.remove("traceId");
                })
                .then(); // 返回Mono<Void>以保持方法签名一致
    }

    /**
     * 获取客户端真实IP地址
     * 
     * IP获取策略（按优先级排序）：
     * 1. X-Forwarded-For: 代理服务器转发的客户端IP（可能有多个，取第一个）
     * 2. X-Real-IP: Nginx等代理设置的客户端真实IP
     * 3. RemoteAddress: 直接连接的客户端IP（没有代理的情况）
     * 
     * 为什么需要这个方法？
     * - 在微服务架构中，请求通常经过多个代理（负载均衡器、网关等）
     * - 直接使用RemoteAddress会得到代理服务器的IP，而不是真实客户端IP
     * - 通过检查HTTP头信息可以获取真实的客户端IP
     * 
     * @param request HTTP请求对象
     * @return 客户端真实IP地址，如果无法获取则返回"unknown"
     */
    private String getClientIp(ServerHttpRequest request) {
        // 1. 检查X-Forwarded-For头（最常用，包含经过的代理链）
        String xForwardedFor = request.getHeaders().getFirst("X-Forwarded-For");
        if (xForwardedFor != null && !xForwardedFor.isEmpty()) {
            // X-Forwarded-For可能包含多个IP，格式：client, proxy1, proxy2
            // 我们取第一个IP，即真实客户端IP
            return xForwardedFor.split(",")[0].trim();
        }
        
        // 2. 检查X-Real-IP头（Nginx等代理常用）
        String xRealIp = request.getHeaders().getFirst("X-Real-IP");
        if (xRealIp != null && !xRealIp.isEmpty()) {
            return xRealIp;
        }
        
        // 3. 使用直接连接的IP地址（没有代理的情况）
        return request.getRemoteAddress() != null ? 
                request.getRemoteAddress().getAddress().getHostAddress() : "unknown";
    }

    /**
     * 获取过滤器的执行顺序
     * 
     * 返回值说明：
     * - Ordered.HIGHEST_PRECEDENCE: 最高优先级（最小整数值）
     * - 数值越小，优先级越高，执行越早
     * 
     * 为什么设置为最高优先级？
     * - 日志过滤器应该尽早执行，以便记录所有请求的完整生命周期
     * - 确保追踪ID在整个请求处理过程中都可用
     * - 避免其他过滤器中的异常影响日志记录
     * 
     * @return 过滤器优先级（数值越小优先级越高）
     */
    @Override
    public int getOrder() {
        return Ordered.HIGHEST_PRECEDENCE;
    }
}
