package org.example.log.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor;

import java.util.concurrent.Executor;
import java.util.concurrent.ThreadPoolExecutor;

/**
 * @author eangus
 */
@Configuration
//针对指定了 @Async("operationLogExecutor") ->就启用异步代理
@EnableAsync
public class LogAsyncConfig {

    @Bean("operationLogExecutor")
    public Executor operationLogExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(2);
        executor.setMaxPoolSize(4);
        executor.setQueueCapacity(500);
        executor.setThreadNamePrefix("op-log-");
        //DiscardPolicy:日志丢了可以接受，业务不能慢->志线程池满了 → 直接丢
        executor.setRejectedExecutionHandler(new ThreadPoolExecutor.DiscardPolicy());
        executor.initialize();
        return executor;
    }
}
