package org.finger.handler;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.slf4j.MDC;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.server.reactive.ServerHttpResponse;
import org.springframework.mock.http.server.reactive.MockServerHttpRequest;
import org.springframework.mock.web.server.MockServerWebExchange;
import org.springframework.web.server.ResponseStatusException;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;
import reactor.test.StepVerifier;

import java.net.ConnectException;
import java.util.concurrent.TimeoutException;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

/**
 * GlobalExceptionHandler 单元测试类
 * 
 * 测试覆盖范围：
 * 1. 各种异常类型的HTTP状态码映射
 * 2. 错误响应的JSON格式验证
 * 3. 追踪ID的处理逻辑
 * 4. 错误消息的提取策略
 * 5. 响应头的设置验证
 */
@ExtendWith(MockitoExtension.class)
@DisplayName("全局异常处理器测试")
public class GlobalExceptionHandlerTest {

    @InjectMocks
    private GlobalExceptionHandler globalExceptionHandler;

    private ServerWebExchange exchange;
    private ServerHttpResponse response;

    @BeforeEach
    void setUp() {
        // 清理MDC，确保测试环境干净
        MDC.clear();
        
        // 创建Mock的ServerWebExchange
        MockServerHttpRequest request = MockServerHttpRequest
                .get("http://localhost:8080/api/test")
                .header("User-Agent", "Test-Agent")
                .build();
        
        exchange = MockServerWebExchange.from(request);
        response = exchange.getResponse();
    }

    @Test
    @DisplayName("测试ResponseStatusException异常处理")
    void testResponseStatusExceptionHandling() {
        // 准备测试数据
        String testMessage = "测试响应状态异常";
        ResponseStatusException exception = new ResponseStatusException(HttpStatus.BAD_REQUEST, testMessage);

        // 执行测试
        Mono<Void> result = globalExceptionHandler.handle(exchange, exception);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证响应状态码
        assertEquals(HttpStatus.BAD_REQUEST, response.getStatusCode());
        
        // 验证响应头
        assertEquals(MediaType.APPLICATION_JSON, response.getHeaders().getContentType());
        assertTrue(response.getHeaders().containsKey("X-Trace-Id"));
    }

    @Test
    @DisplayName("测试TimeoutException异常处理")
    void testTimeoutExceptionHandling() {
        // 准备测试数据
        TimeoutException exception = new TimeoutException("请求超时");

        // 执行测试
        Mono<Void> result = globalExceptionHandler.handle(exchange, exception);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证响应状态码
        assertEquals(HttpStatus.GATEWAY_TIMEOUT, response.getStatusCode());
        
        // 验证响应头
        assertEquals(MediaType.APPLICATION_JSON, response.getHeaders().getContentType());
        assertTrue(response.getHeaders().containsKey("X-Trace-Id"));
    }

    @Test
    @DisplayName("测试ConnectException异常处理")
    void testConnectExceptionHandling() {
        // 准备测试数据
        ConnectException exception = new ConnectException("连接失败");

        // 执行测试
        Mono<Void> result = globalExceptionHandler.handle(exchange, exception);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证响应状态码
        assertEquals(HttpStatus.BAD_GATEWAY, response.getStatusCode());
    }

    @Test
    @DisplayName("测试通用异常处理")
    void testGenericExceptionHandling() {
        // 准备测试数据
        RuntimeException exception = new RuntimeException("系统内部错误");

        // 执行测试
        Mono<Void> result = globalExceptionHandler.handle(exchange, exception);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证响应状态码
        assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, response.getStatusCode());
    }

    @Test
    @DisplayName("测试带MDC追踪ID的异常处理")
    void testExceptionHandlingWithMdcTraceId() {
        // 设置MDC中的追踪ID
        String mdcTraceId = "mdc-trace-id-123";
        MDC.put("traceId", mdcTraceId);
        
        // 准备测试数据
        RuntimeException exception = new RuntimeException("测试异常");

        // 执行测试
        Mono<Void> result = globalExceptionHandler.handle(exchange, exception);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证响应头中的追踪ID
        String traceId = response.getHeaders().getFirst("X-Trace-Id");
        assertEquals(mdcTraceId, traceId);
        
        // 清理MDC
        MDC.clear();
    }

    @Test
    @DisplayName("测试空消息异常的处理")
    void testExceptionWithEmptyMessage() {
        // 准备测试数据 - 空消息的异常
        RuntimeException exception = new RuntimeException("");

        // 执行测试
        Mono<Void> result = globalExceptionHandler.handle(exchange, exception);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证响应状态码
        assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, response.getStatusCode());
    }

    @Test
    @DisplayName("测试null消息异常的处理")
    void testExceptionWithNullMessage() {
        // 准备测试数据 - null消息的异常
        RuntimeException exception = new RuntimeException((String) null);

        // 执行测试
        Mono<Void> result = globalExceptionHandler.handle(exchange, exception);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证响应状态码
        assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, response.getStatusCode());
    }

    @Test
    @DisplayName("测试异常状态码映射逻辑")
    void testExceptionStatusMapping() {
        // 测试不同的异常类型映射到正确的HTTP状态码
        assertEquals(HttpStatus.BAD_REQUEST, 
                    globalExceptionHandler.determineHttpStatus(
                        new ResponseStatusException(HttpStatus.BAD_REQUEST)));
        
        assertEquals(HttpStatus.GATEWAY_TIMEOUT, 
                    globalExceptionHandler.determineHttpStatus(
                        new TimeoutException()));
        
        assertEquals(HttpStatus.BAD_GATEWAY, 
                    globalExceptionHandler.determineHttpStatus(
                        new ConnectException()));
        
        assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, 
                    globalExceptionHandler.determineHttpStatus(
                        new RuntimeException()));
    }

    @Test
    @DisplayName("测试错误消息提取逻辑")
    void testErrorMessageExtraction() {
        // 测试ResponseStatusException的消息提取
        ResponseStatusException responseException = 
            new ResponseStatusException(HttpStatus.NOT_FOUND, "资源未找到");
        assertEquals("资源未找到", 
                    globalExceptionHandler.getErrorMessage(responseException));
        
        // 测试普通异常的消息提取
        RuntimeException runtimeException = new RuntimeException("运行时错误");
        assertEquals("运行时错误", 
                    globalExceptionHandler.getErrorMessage(runtimeException));
        
        // 测试空消息异常的处理
        RuntimeException emptyException = new RuntimeException("");
        assertEquals("An unexpected error occurred", 
                    globalExceptionHandler.getErrorMessage(emptyException));
        
        // 测试null消息异常的处理
        RuntimeException nullException = new RuntimeException((String) null);
        assertEquals("An unexpected error occurred", 
                    globalExceptionHandler.getErrorMessage(nullException));
    }
}
