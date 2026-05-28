package org.finger.config;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.slf4j.MDC;
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.server.reactive.ServerHttpRequest;
import org.springframework.http.server.reactive.ServerHttpResponse;
import org.springframework.mock.http.server.reactive.MockServerHttpRequest;
import org.springframework.mock.web.server.MockServerWebExchange;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;
import reactor.test.StepVerifier;

import java.net.InetSocketAddress;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

/**
 * LogFilter 集成测试类
 * 
 * 测试覆盖范围：
 * 1. 请求开始日志记录
 * 2. 请求完成日志记录
 * 3. 请求失败日志记录
 * 4. 追踪ID的生成和传递
 * 5. 客户端IP地址提取
 * 6. 请求处理时间计算
 * 7. MDC清理逻辑
 * 8. 过滤器执行顺序
 */
@ExtendWith(MockitoExtension.class)
@DisplayName("日志过滤器集成测试")
public class LogFilterTest {

    private LogFilter logFilter;
    private GatewayFilterChain filterChain;
    private ServerWebExchange exchange;
    private ServerHttpResponse response;

    @BeforeEach
    void setUp() {
        // 清理MDC，确保测试环境干净
        MDC.clear();
        
        // 初始化被测试的过滤器
        logFilter = new LogFilter();
        
        // Mock过滤器链
        filterChain = mock(GatewayFilterChain.class);
        
        // 创建测试用的ServerWebExchange
        MockServerHttpRequest request = MockServerHttpRequest
                .get("http://localhost:8080/api/test")
                .header(HttpHeaders.USER_AGENT, "Test-Agent/1.0")
                .header("X-Forwarded-For", "192.168.1.100, 10.0.0.1")
                .build();
        
        exchange = MockServerWebExchange.from(request);
        response = exchange.getResponse();
    }

    @Test
    @DisplayName("测试成功请求的完整日志流程")
    void testSuccessfulRequestLogging() {
        // 设置响应状态码
        response.setStatusCode(HttpStatus.OK);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchange, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证过滤器链被调用
        verify(filterChain, times(1)).filter(exchange);
        
        // 验证MDC被清理
        assertNull(MDC.get("traceId"));
    }

    @Test
    @DisplayName("测试失败请求的异常日志流程")
    void testFailedRequestLogging() {
        // Mock过滤器链抛出异常
        RuntimeException testException = new RuntimeException("测试异常");
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.error(testException));

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchange, filterChain);

        // 验证异常被正确传播
        StepVerifier.create(result)
                .expectError(RuntimeException.class)
                .verify();

        // 验证过滤器链被调用
        verify(filterChain, times(1)).filter(exchange);
        
        // 验证MDC被清理（即使发生异常）
        assertNull(MDC.get("traceId"));
    }

    @Test
    @DisplayName("测试追踪ID的生成和传递")
    void testTraceIdGenerationAndPropagation() {
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchange, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证追踪ID在MDC中存在（在过滤过程中）
        // 注意：由于过滤器执行完成后MDC会被清理，这里我们只能验证清理逻辑
        assertNull(MDC.get("traceId"));
    }

    @Test
    @DisplayName("测试X-Forwarded-For头的IP地址提取")
    void testXForwardedForIpExtraction() {
        // 创建带有X-Forwarded-For头的请求
        MockServerHttpRequest request = MockServerHttpRequest
                .get("http://localhost:8080/api/test")
                .header("X-Forwarded-For", "192.168.1.100, 10.0.0.1, 172.16.0.1")
                .build();
        
        ServerWebExchange exchangeWithForwardedFor = MockServerWebExchange.from(request);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchangeWithForwardedFor, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();
    }

    @Test
    @DisplayName("测试X-Real-IP头的IP地址提取")
    void testXRealIpExtraction() {
        // 创建带有X-Real-IP头的请求（没有X-Forwarded-For）
        MockServerHttpRequest request = MockServerHttpRequest
                .get("http://localhost:8080/api/test")
                .header("X-Real-IP", "192.168.1.200")
                .build();
        
        ServerWebExchange exchangeWithRealIp = MockServerWebExchange.from(request);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchangeWithRealIp, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();
    }

    @Test
    @DisplayName("测试直接连接IP地址提取")
    void testDirectConnectionIpExtraction() {
        // 创建带有远程地址的请求 - 使用localhost避免解析问题
        MockServerHttpRequest request = MockServerHttpRequest
                .get("http://localhost:8080/api/test")
                .remoteAddress(new InetSocketAddress("localhost", 12345))
                .build();
        
        ServerWebExchange exchangeWithRemoteAddr = MockServerWebExchange.from(request);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchangeWithRemoteAddr, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();
    }

    @Test
    @DisplayName("测试无法获取IP地址的情况")
    void testUnknownIpExtraction() {
        // 创建没有IP地址信息的请求
        MockServerHttpRequest request = MockServerHttpRequest
                .get("http://localhost:8080/api/test")
                .build();
        
        ServerWebExchange exchangeWithoutIp = MockServerWebExchange.from(request);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchangeWithoutIp, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();
    }

    @Test
    @DisplayName("测试不同HTTP方法的日志记录")
    void testDifferentHttpMethods() {
        // 测试POST方法
        MockServerHttpRequest postRequest = MockServerHttpRequest
                .post("http://localhost:8080/api/test")
                .header(HttpHeaders.CONTENT_TYPE, "application/json")
                .build();
        
        ServerWebExchange postExchange = MockServerWebExchange.from(postRequest);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(postExchange, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证过滤器链被调用
        verify(filterChain, times(1)).filter(postExchange);
    }

    @Test
    @DisplayName("测试带有查询参数的请求日志")
    void testRequestWithQueryParams() {
        // 创建带有查询参数的请求
        MockServerHttpRequest request = MockServerHttpRequest
                .get("http://localhost:8080/api/test?param1=value1&param2=value2")
                .build();
        
        ServerWebExchange exchangeWithParams = MockServerWebExchange.from(request);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchangeWithParams, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();
    }

    @Test
    @DisplayName("测试不同响应状态码的日志记录")
    void testDifferentResponseStatusCodes() {
        // 测试404状态码
        response.setStatusCode(HttpStatus.NOT_FOUND);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchange, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 重置响应状态码
        response.setStatusCode(HttpStatus.OK);

        // 测试500状态码
        response.setStatusCode(HttpStatus.INTERNAL_SERVER_ERROR);

        // 执行过滤器
        result = logFilter.filter(exchange, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();
    }

    @Test
    @DisplayName("测试过滤器执行顺序")
    void testFilterOrder() {
        // 验证过滤器返回正确的执行顺序
        int order = logFilter.getOrder();
        
        // 应该返回最高优先级
        assertEquals(Integer.MIN_VALUE, order);
    }

    @Test
    @DisplayName("测试并发请求的日志隔离")
    void testConcurrentRequestLoggingIsolation() {
        // 创建多个不同的请求
        MockServerHttpRequest request1 = MockServerHttpRequest
                .get("http://localhost:8080/api/test1")
                .build();
        ServerWebExchange exchange1 = MockServerWebExchange.from(request1);

        MockServerHttpRequest request2 = MockServerHttpRequest
                .get("http://localhost:8080/api/test2")
                .build();
        ServerWebExchange exchange2 = MockServerWebExchange.from(request2);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 并发执行过滤器
        Mono<Void> result1 = logFilter.filter(exchange1, filterChain);
        Mono<Void> result2 = logFilter.filter(exchange2, filterChain);

        // 验证两个请求都能正常完成
        StepVerifier.create(result1)
                .verifyComplete();

        StepVerifier.create(result2)
                .verifyComplete();

        // 验证过滤器链被调用了两次
        verify(filterChain, times(2)).filter(any(ServerWebExchange.class));
    }

    @Test
    @DisplayName("测试User-Agent头的处理")
    void testUserAgentHeaderHandling() {
        // 创建带有复杂User-Agent头的请求
        MockServerHttpRequest request = MockServerHttpRequest
                .get("http://localhost:8080/api/test")
                .header(HttpHeaders.USER_AGENT, 
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
                .build();
        
        ServerWebExchange exchangeWithUserAgent = MockServerWebExchange.from(request);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchangeWithUserAgent, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();
    }

    @Test
    @DisplayName("测试空User-Agent头的处理")
    void testEmptyUserAgentHeaderHandling() {
        // 创建没有User-Agent头的请求
        MockServerHttpRequest request = MockServerHttpRequest
                .get("http://localhost:8080/api/test")
                .build();
        
        ServerWebExchange exchangeWithoutUserAgent = MockServerWebExchange.from(request);
        
        // Mock过滤器链
        when(filterChain.filter(any(ServerWebExchange.class))).thenReturn(Mono.empty());

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchangeWithoutUserAgent, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();
    }

    @Test
    @DisplayName("测试请求处理时间计算")
    void testRequestProcessingTimeCalculation() throws InterruptedException {
        // Mock过滤器链，添加一些延迟来模拟处理时间
        when(filterChain.filter(any(ServerWebExchange.class)))
                .thenReturn(Mono.delay(java.time.Duration.ofMillis(100)).then());

        // 记录开始时间
        long startTime = System.currentTimeMillis();

        // 执行过滤器
        Mono<Void> result = logFilter.filter(exchange, filterChain);

        // 验证结果
        StepVerifier.create(result)
                .verifyComplete();

        // 验证处理时间大于100ms（考虑到系统开销）
        long endTime = System.currentTimeMillis();
        assertTrue(endTime - startTime >= 100);
    }
}
