package org.finger.handler;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.slf4j.MDC;
import org.springframework.boot.web.reactive.error.ErrorWebExceptionHandler;
import org.springframework.core.annotation.Order;
import org.springframework.core.io.buffer.DataBuffer;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.server.reactive.ServerHttpResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

/**
 * 全局异常处理器
 * 
 * 功能说明：
 * 1. 统一处理网关中的所有异常
 * 2. 生成标准化的错误响应格式
 * 3. 记录详细的错误日志，包含追踪ID
 * 4. 根据异常类型返回合适的HTTP状态码
 * 
 * @Order(-1) 确保该处理器具有最高优先级
 */
@Component
@Order(-1)
public class GlobalExceptionHandler implements ErrorWebExceptionHandler {

    /** 日志记录器 */
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);
    
    /** JSON序列化器，用于将错误响应转换为JSON格式 */
    private final ObjectMapper objectMapper = new ObjectMapper();

    /**
     * 处理所有异常的核心方法
     * 
     * 处理流程：
     * 1. 获取或生成追踪ID（用于链路追踪）
     * 2. 记录详细的错误日志
     * 3. 根据异常类型确定HTTP状态码
     * 4. 设置响应头（JSON格式、追踪ID）
     * 5. 构建标准化的错误响应体
     * 6. 将响应写入HTTP响应流
     * 
     * @param exchange 服务器Web交换对象，包含请求和响应信息
     * @param ex 发生的异常对象
     * @return Mono<Void> 异步处理完成信号
     */
    @Override
    public Mono<Void> handle(ServerWebExchange exchange, Throwable ex) {
        
        // 1. 获取追踪ID，用于链路追踪和日志关联
        String traceId = MDC.get("traceId");
        if (traceId == null) {
            // 如果MDC中没有追踪ID，则使用请求ID作为备选方案
            traceId = exchange.getRequest().getId() != null ? 
                    exchange.getRequest().getId().toString() : "unknown";
        }

        // 2. 记录详细的错误日志，包含追踪ID、请求路径和异常信息
        logger.error("Gateway Error - TraceId: {}, Path: {}, Error: {}", 
                traceId, 
                exchange.getRequest().getURI().getPath(), 
                ex.getMessage(), 
                ex);

        // 3. 获取HTTP响应对象
        ServerHttpResponse response = exchange.getResponse();
        
        // 4. 根据异常类型确定合适的HTTP状态码
        HttpStatus status = determineHttpStatus(ex);
        response.setStatusCode(status);
        
        // 5. 设置响应头
        response.getHeaders().setContentType(MediaType.APPLICATION_JSON); // 设置内容类型为JSON
        response.getHeaders().add("X-Trace-Id", traceId); // 添加追踪ID到响应头

        // 6. 构建标准化的错误响应体
        Map<String, Object> errorResponse = new HashMap<>();
        errorResponse.put("timestamp", LocalDateTime.now().toString()); // 错误发生时间
        errorResponse.put("status", status.value()); // HTTP状态码
        errorResponse.put("error", status.getReasonPhrase()); // 错误描述
        errorResponse.put("message", getErrorMessage(ex)); // 用户友好的错误消息
        errorResponse.put("path", exchange.getRequest().getURI().getPath()); // 请求路径
        errorResponse.put("traceId", traceId); // 追踪ID

        // 7. 将错误响应对象序列化为JSON字符串
        String errorJson;
        try {
            errorJson = objectMapper.writeValueAsString(errorResponse);
        } catch (JsonProcessingException e) {
            // 如果JSON序列化失败，使用简单的错误格式
            errorJson = "{\"error\":\"Internal Server Error\",\"message\":\"Error processing error response\"}";
        }

        // 8. 将JSON字符串包装为DataBuffer并写入响应流
        DataBuffer buffer = response.bufferFactory().wrap(errorJson.getBytes());
        return response.writeWith(Mono.just(buffer));
    }

    /**
     * 根据异常类型确定HTTP状态码
     * 
     * 异常类型映射：
     * - ResponseStatusException: 使用异常中定义的状态码
     * - TimeoutException: 网关超时 (504)
     * - ConnectException: 后端服务不可用 (502)
     * - NotFoundException: 资源未找到 (404)
     * - UnsupportedMediaTypeStatusException: 不支持的媒体类型 (415)
     * - MethodNotAllowedException: 方法不允许 (405)
     * - 其他异常: 内部服务器错误 (500)
     * 
     * @param ex 异常对象
     * @return 对应的HTTP状态码
     */
    protected HttpStatus determineHttpStatus(Throwable ex) {
        // Spring Web的响应状态异常 - 使用异常中定义的状态码
        if (ex instanceof org.springframework.web.server.ResponseStatusException) {
            return HttpStatus.resolve(((org.springframework.web.server.ResponseStatusException) ex).getStatusCode().value());
        }
        
        // 超时异常 - 网关超时
        if (ex instanceof java.util.concurrent.TimeoutException) {
            return HttpStatus.GATEWAY_TIMEOUT;
        }
        
        // 连接异常 - 后端服务不可用
        if (ex instanceof java.net.ConnectException) {
            return HttpStatus.BAD_GATEWAY;
        }
        
        // Spring Gateway未找到异常 - 资源未找到
        if (ex instanceof org.springframework.cloud.gateway.support.NotFoundException) {
            return HttpStatus.NOT_FOUND;
        }
        
        // 不支持的媒体类型异常
        if (ex instanceof org.springframework.web.server.UnsupportedMediaTypeStatusException) {
            return HttpStatus.UNSUPPORTED_MEDIA_TYPE;
        }
        
        // 方法不允许异常
        if (ex instanceof org.springframework.web.server.MethodNotAllowedException) {
            return HttpStatus.METHOD_NOT_ALLOWED;
        }
        
        // 默认情况 - 内部服务器错误
        return HttpStatus.INTERNAL_SERVER_ERROR;
    }

    /**
     * 获取用户友好的错误消息
     * 
     * 消息获取策略：
     * 1. ResponseStatusException: 使用异常中的reason信息
     * 2. 其他异常: 使用异常的message（如果不为空）
     * 3. 默认情况: 返回通用错误消息
     * 
     * @param ex 异常对象
     * @return 用户友好的错误消息
     */
    protected String getErrorMessage(Throwable ex) {
        // ResponseStatusException - 使用异常中定义的reason
        if (ex instanceof org.springframework.web.server.ResponseStatusException) {
            return ((org.springframework.web.server.ResponseStatusException) ex).getReason();
        }
        
        // 其他异常 - 使用异常消息（如果不为空）
        if (ex.getMessage() != null && !ex.getMessage().isEmpty()) {
            return ex.getMessage();
        }
        
        // 默认情况 - 返回通用错误消息
        return "An unexpected error occurred";
    }
}
