package org.export.limiter;

import jakarta.annotation.Resource;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Component;

import java.util.concurrent.TimeUnit;

/**
 * @author aengus
 * 控制导出接口的访问频率
 */
@Component
public class ExportLimiter {

    @Resource
    private StringRedisTemplate redis;

    private static final String USER_KEY_PREFIX = "export:user:";
    private static final String GLOBAL_KEY = "export:global";

    /**
     * 用户级限制（防重复提交）
     */
    public boolean tryUser(String userId) {
        String key = USER_KEY_PREFIX + userId;
        return safeSetIfAbsent(key, 5, TimeUnit.SECONDS);
    }

    /**
     * 全局限制（简单锁模型）
     */
    public boolean tryGlobal() {
        return safeSetIfAbsent(GLOBAL_KEY, 60, TimeUnit.SECONDS);
    }

    /**
     * 释放全局锁（必须配合 tryGlobal 使用）
     */
    public void releaseGlobal() {
        redis.delete(GLOBAL_KEY);
    }

    /**
     * 释放用户锁（推荐任务完成后调用）
     */
    public void releaseUser(String userId) {
        redis.delete(USER_KEY_PREFIX + userId);
    }

    /**
     * 安全 setIfAbsent（核心方法）
     * 解决：历史 key 没有 TTL 的问题
     */
    public boolean safeSetIfAbsent(String key, long timeout, TimeUnit unit) {
        Boolean success = redis.opsForValue().setIfAbsent(key, "1", timeout, unit);

        //兜底修复 TTL（防止历史脏数据）
        Long ttl = redis.getExpire(key);
        if (ttl <= 0) {
            redis.expire(key, timeout, unit);
        }
        return Boolean.TRUE.equals(success);
    }
}