# Gateway Service

基于Spring Cloud Gateway的微服务网关，提供统一的API入口和强大的功能特性。

## 功能特性

### ✅ 路由转发
- 支持多服务路由配置
- 灵活的路径匹配规则
- 负载均衡和服务发现

### ✅ 鉴权拦截
- JWT Token验证
- 支持白名单路径配置
- 用户信息传递给下游服务

### ✅ 日志记录
- 结构化日志输出
- 请求追踪ID (TraceId)
- 完整的请求生命周期记录
- 支持文件和控制台输出

### ✅ 限流（Redis）
- 基于Redis的分布式限流
- 支持多种限流策略（IP、用户ID、API Key）
- 可配置的限流参数

### ✅ 跨域支持
- 完整的CORS配置
- 生产环境友好的配置选项
- 支持预检请求缓存

## 技术栈

- Spring Boot 3.4.5
- Spring Cloud Gateway
- Spring Cloud Alibaba
- Redis
- JWT
- SLF4J + Logback

## 配置说明

### 基础配置
```yaml
server:
  port: 8080

spring:
  application:
    name: gateway-service
```

### Redis配置
```yaml
spring:
  redis:
    host: localhost
    port: 6379
    timeout: 2000ms
    lettuce:
      pool:
        max-active: 8
        max-idle: 8
        min-idle: 0
```

### 路由配置
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: user-service
          uri: http://localhost:8081
          predicates:
            - Path=/user/**
          filters:
            - StripPrefix=1
            - name: RequestRateLimiter
              args:
                redis-rate-limiter.replenishRate: 20
                redis-rate-limiter.burstCapacity: 40
                key-resolver: "#{@userKeyResolver}"
```

### 限流配置
- **replenishRate**: 每秒补充的令牌数
- **burstCapacity**: 令牌桶容量
- **key-resolver**: 限流键解析器

### CORS配置
```yaml
cors:
  allowed-origins: "*" # 生产环境配置具体域名
  allowed-methods: "GET,POST,PUT,DELETE,OPTIONS"
  allowed-headers: "*"
  allow-credentials: false
  max-age: 3600
```

### JWT配置
```yaml
jwt:
  secret: "bXlTZWNyZXRLZXkxMjM0NTY3ODkwYWJjZGVmZ2hpams="
```

## 限流策略

### 1. IP限流
基于客户端IP地址进行限流，适用于匿名用户访问。

### 2. 用户限流
基于用户ID进行限流，适用于已认证用户的精细化控制。

### 3. API Key限流
基于API Key进行限流，适用于第三方服务调用。

## 日志格式

日志采用结构化格式，包含以下信息：
- **TraceId**: 请求追踪ID
- **Timestamp**: 时间戳
- **Method**: HTTP方法
- **URI**: 请求路径
- **ClientIP**: 客户端IP
- **Duration**: 请求耗时
- **StatusCode**: 响应状态码

## 鉴权机制

### JWT验证流程
1. 客户端在请求头中携带JWT Token
2. 网关验证Token的有效性
3. 解析用户信息并传递给下游服务
4. 对无效Token返回401状态码

### 白名单路径
以下路径无需鉴权：
- `/login/**`
- `/register/**`
- `/public/**`
- `/health`
- `/actuator/**`

## 错误处理

网关提供统一的错误处理机制：
- 结构化的错误响应
- 包含TraceId便于问题追踪
- 根据异常类型返回适当的HTTP状态码

## 监控端点

启用以下管理端点：
- `/actuator/health`: 健康检查
- `/actuator/info`: 应用信息
- `/actuator/metrics`: 性能指标
- `/actuator/prometheus`: Prometheus指标

## 部署说明

### 环境要求
- Java 17+
- Redis 6.0+
- Maven 3.6+

### 启动命令
```bash
mvn spring-boot:run
```

### Docker部署
```bash
docker build -t gateway-service .
docker run -p 8080:8080 gateway-service
```

## 快速开始

### 本地运行

1. **启动Redis**
```bash
# Docker方式（推荐）
docker run -d -p 6379:6379 redis:latest

# 或本地Redis
redis-server
```

2. **启动网关服务**
```bash
mvn clean spring-boot:run
```

3. **测试健康检查**
```bash
curl http://localhost:8080/health
```

## 实践指南

### 1. 配置后端服务
在 `application.yml` 中添加你的微服务路由：
```yaml
spring:
  cloud:
    gateway:
      routes:
        - id: your-service
          uri: http://localhost:9090    # 你的服务地址
          predicates:
            - Path=/your-api/**         # 路径匹配
          filters:
            - StripPrefix=1             # 剥离前缀
            - name: RequestRateLimiter
              args:
                redis-rate-limiter.replenishRate: 10
                redis-rate-limiter.burstCapacity: 20
                key-resolver: "#{@ipKeyResolver}"
```

### 2. 获取JWT Token（示例）
```bash
# 调用登录服务获取Token
curl -X POST http://localhost:8080/login/auth \
  -H "Content-Type: application/json" \
  -d '{"username":"user","password":"pass"}'

# 响应示例: {"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}
```

### 3. 使用Token访问受保护的服务
```bash
curl -H "Authorization: Bearer YOUR_TOKEN" \
     http://localhost:8080/user/profile
```

### 4. 查看TraceId追踪日志
```bash
# 从日志中查找对应的TraceId
tail -f logs/gateway-service.log | grep "a1b2c3d4e5f6"
```

## 生产部署清单

- [ ] 设置环境变量 `JWT_SECRET`（使用强密钥）
- [ ] 设置环境变量 `CORS_ALLOWED_ORIGINS`（配置实际域名）
- [ ] 调整Redis连接池参数 (`max-active`, `max-idle`)
- [ ] 根据流量调整限流参数 (`replenishRate`, `burstCapacity`)
- [ ] 启用日志持久化和轮转
- [ ] 配置监控告警（/actuator/metrics）
- [ ] 验证所有后端服务地址和健康状态
- [ ] 测试JWT过期和刷新流程
- [ ] 验证CORS跨域配置
- [ ] 性能测试和压力测试

## 常见问题

### 限流不生效？
检查Redis连接状态，查看日志中是否有Redis连接错误。

### 下游服务收不到用户信息？
确保JWT Token有效，检查请求头中是否包含 `X-User-Id`、`X-User-Name` 等。

### CORS跨域报错？
检查前端请求源是否在 `CORS_ALLOWED_ORIGINS` 配置中。

### 如何追踪请求链路？
每个请求都有唯一的TraceId，在日志中搜索该ID即可看到完整链路。

## 注意事项

1. **生产环境配置**
   - 必须设置 `JWT_SECRET` 环境变量为强密钥
   - 必须设置 `CORS_ALLOWED_ORIGINS` 为具体的域名
   - 调整Redis连接池参数以应对生产流量

2. **性能优化**
   - 根据业务需求调整限流参数
   - 配置合适的日志级别
   - 监控Redis连接状态和网关吞吐量

3. **安全考虑**
   - 定期轮换JWT密钥
   - 启用HTTPS/TLS加密
   - 配置防火墙规则，限制网关访问
   - 不要在日志中输出敏感信息（Token、密码等）

## 代码修复记录

已修复以下问题：
1. ✅ **GlobalAuthFilter**: 修复请求头修改不生效问题 - 使用正确的 `exchange.mutate()` API
2. ✅ **RateLimitConfig**: 修复IP提取逻辑 - 正确处理多个IP的情况
3. ✅ **安全配置**: JWT密钥和CORS配置从环境变量读取
4. ✅ **代码注释**: 添加详细的代码注释便于维护
