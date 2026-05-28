# Gateway Service 部署指南

本文档说明如何在开发、测试和生产环境中部署网关服务。

## 开发环境

### 快速启动（本地）

1. **启动Redis**
```bash
# 使用Docker
docker run -d -p 6379:6379 --name redis-dev redis:latest

# 或使用本地Redis
redis-server
```

2. **运行网关服务**
```bash
# 方式1：使用Maven
mvn clean spring-boot:run

# 方式2：使用IDE (IntelliJ IDEA)
右键 -> Run 'GatewayServiceApplication.main()'
```

3. **验证服务**
```bash
curl http://localhost:8080/health
```

### 使用Docker Compose（推荐）

```bash
# 启动所有服务
docker-compose up -d

# 查看日志
docker-compose logs -f gateway

# 停止服务
docker-compose down
```

---

## 测试环境

### 部署步骤

1. **构建Docker镜像**
```bash
# 构建镜像
docker build -t gateway-service:test .

# 查看镜像
docker images | grep gateway-service
```

2. **准备环境变量**
```bash
# 复制环境变量模板
cp .env.example .env

# 编辑配置，使用测试环境的值
# - JWT_SECRET: 使用测试密钥
# - CORS_ALLOWED_ORIGINS: 配置测试域名
# - 后端服务地址: 指向测试环境服务器
```

3. **启动Redis（测试环境）**
```bash
docker run -d \
  --name redis-test \
  -p 6379:6379 \
  -e REDIS_PASSWORD=test_redis_pass \
  redis:7-alpine \
  redis-server --requirepass test_redis_pass
```

4. **启动网关服务**
```bash
docker run -d \
  --name gateway-test \
  -p 8080:8080 \
  --link redis-test:redis \
  --env-file .env \
  gateway-service:test
```

5. **执行测试**
```bash
# 健康检查
curl http://localhost:8080/health

# 测试CORS
curl -H "Origin: http://test.domain.com" http://localhost:8080/health

# 测试限流
for i in {1..50}; do curl http://localhost:8080/health; done
```

---

## 生产环境

### 生产环境配置清单

#### 安全配置
- [ ] 使用强密钥生成JWT密钥（至少32字节）
```bash
# 生成随机密钥
openssl rand -base64 32
```
- [ ] 设置环境变量 `JWT_SECRET`（不要硬编码在代码中）
- [ ] 配置CORS_ALLOWED_ORIGINS为实际域名（不使用 `*`）
- [ ] 启用HTTPS/TLS加密
- [ ] 配置防火墙规则，限制网关访问

#### 性能优化
- [ ] 调整Redis连接池参数
```yaml
spring:
  redis:
    lettuce:
      pool:
        max-active: 32      # 根据并发量调整
        max-idle: 16
        min-idle: 8
```
- [ ] 调整限流参数（根据预期流量）
- [ ] 配置日志级别为INFO（关闭DEBUG）
- [ ] 启用日志异步输出

#### 监控告警
- [ ] 启用Prometheus metrics：`/actuator/prometheus`
- [ ] 配置告警规则（CPU、内存、响应时间等）
- [ ] 监控Redis连接状态
- [ ] 监控限流触发率

### 生产部署方式

#### 方式1：Kubernetes（K8s）

1. **构建镜像并上传到镜像仓库**
```bash
# 构建镜像
docker build -t registry.example.com/gateway-service:1.0.0 .

# 推送到镜像仓库
docker push registry.example.com/gateway-service:1.0.0
```

2. **创建K8s Deployment**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gateway-service
  namespace: production
spec:
  replicas: 3  # 根据流量调整副本数
  selector:
    matchLabels:
      app: gateway-service
  template:
    metadata:
      labels:
        app: gateway-service
    spec:
      containers:
      - name: gateway
        image: registry.example.com/gateway-service:1.0.0
        ports:
        - containerPort: 8080
        env:
        - name: JWT_SECRET
          valueFrom:
            secretKeyRef:
              name: gateway-secrets
              key: jwt-secret
        - name: CORS_ALLOWED_ORIGINS
          value: "https://yourdomain.com"
        - name: SPRING_REDIS_HOST
          value: "redis-service"
        - name: SPRING_REDIS_PORT
          value: "6379"
        # 资源限制
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        # 健康检查
        livenessProbe:
          httpGet:
            path: /actuator/health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /actuator/health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: gateway-service
  namespace: production
spec:
  selector:
    app: gateway-service
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
```

3. **部署到K8s**
```bash
# 创建密钥
kubectl create secret generic gateway-secrets \
  --from-literal=jwt-secret="your-jwt-secret" \
  -n production

# 部署应用
kubectl apply -f gateway-deployment.yaml

# 检查部署状态
kubectl get deployments -n production
kubectl get pods -n production
kubectl logs -f deployment/gateway-service -n production
```

#### 方式2：Docker Swarm

```bash
# 初始化Swarm（如果未初始化）
docker swarm init

# 创建Redis服务
docker service create \
  --name redis \
  -p 6379:6379 \
  redis:7-alpine

# 创建网关服务
docker service create \
  --name gateway \
  -p 8080:8080 \
  --env JWT_SECRET="your-jwt-secret" \
  --env CORS_ALLOWED_ORIGINS="https://yourdomain.com" \
  --env SPRING_REDIS_HOST="redis" \
  --replicas 3 \
  gateway-service:latest
```

#### 方式3：虚拟机（VM）

1. **在服务器上安装依赖**
```bash
# 安装Java 17
sudo apt-get update
sudo apt-get install -y openjdk-17-jdk

# 安装Redis
sudo apt-get install -y redis-server

# 启动Redis
sudo systemctl start redis-server
sudo systemctl enable redis-server
```

2. **上传并运行应用**
```bash
# 上传JAR文件
scp gateway-service-0.0.1-SNAPSHOT.jar user@server:/opt/apps/

# SSH登录服务器
ssh user@server

# 设置环境变量
export JWT_SECRET="your-jwt-secret"
export CORS_ALLOWED_ORIGINS="https://yourdomain.com"

# 运行应用
java -jar /opt/apps/gateway-service-0.0.1-SNAPSHOT.jar
```

3. **使用Systemd管理服务**
```bash
# 创建服务文件 /etc/systemd/system/gateway.service
[Unit]
Description=Gateway Service
After=network.target

[Service]
Type=simple
User=app
Environment="JWT_SECRET=your-jwt-secret"
Environment="CORS_ALLOWED_ORIGINS=https://yourdomain.com"
ExecStart=/usr/bin/java -jar /opt/apps/gateway-service-0.0.1-SNAPSHOT.jar
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target

# 启动服务
sudo systemctl start gateway
sudo systemctl enable gateway

# 查看状态
sudo systemctl status gateway
```

---

## 滚动更新（零停机部署）

### K8s环境
```bash
# 更新镜像版本
kubectl set image deployment/gateway-service \
  gateway=registry.example.com/gateway-service:2.0.0 \
  -n production

# 监控更新进度
kubectl rollout status deployment/gateway-service -n production

# 如果需要回滚
kubectl rollout undo deployment/gateway-service -n production
```

### Docker Swarm环境
```bash
# 更新服务镜像
docker service update \
  --image gateway-service:2.0.0 \
  gateway
```

---

## 监控和日志

### 查看日志
```bash
# Docker方式
docker logs -f gateway-service

# K8s方式
kubectl logs -f deployment/gateway-service -n production

# 本地方式
tail -f logs/gateway-service.log
```

### 性能指标
```bash
# 查看Prometheus指标
curl http://localhost:8080/actuator/prometheus

# 查看应用信息
curl http://localhost:8080/actuator/info

# 查看健康状态
curl http://localhost:8080/actuator/health/details
```

---

## 故障排除

### 问题：服务无法启动
```bash
# 检查Java版本
java -version  # 应该是 17+

# 检查Redis连接
redis-cli ping  # 应该返回 PONG

# 查看启动日志
tail -100 logs/gateway-service.log
```

### 问题：限流不生效
```bash
# 检查Redis连接
curl http://localhost:8080/actuator/health/redis

# 检查Redis键
redis-cli KEYS "gateway*"
```

### 问题：请求超时
```bash
# 检查网关日志中的TraceId
grep "TraceId: abc123" logs/gateway-service.log

# 检查下游服务是否正常
curl http://localhost:8081/health  # 用户服务
curl http://localhost:8082/health  # 登录服务
```

---

## 参考资源

- [Spring Cloud Gateway 文档](https://spring.io/projects/spring-cloud-gateway)
- [Redis 文档](https://redis.io/documentation)
- [Docker 文档](https://docs.docker.com/)
- [Kubernetes 文档](https://kubernetes.io/docs/)
