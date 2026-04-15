package org.export.limiter;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Component;

import java.util.concurrent.TimeUnit;

@Component
public class ExportLimiter {

    @Autowired
    private StringRedisTemplate redis;

    public boolean tryUser(String userId) {
        String key = "export:user:" + userId;
        Long c = redis.opsForValue().increment(key);
        if (c == 1) {
            redis.expire(key, 5, TimeUnit.SECONDS);
        }
        return c <= 3;
    }

    public boolean tryGlobal() {
        Long c = redis.opsForValue().increment("export:global");
        return c <= 10;
    }

    public void releaseGlobal() {
        redis.opsForValue().decrement("export:global");
    }
}
