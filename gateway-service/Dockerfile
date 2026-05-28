# 多阶段构建：第一阶段 - 编译
FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY pom.xml .
COPY src src
RUN mvn clean package -DskipTests

# 第二阶段 - 运行
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app

# 从第一阶段复制编译好的JAR文件
COPY --from=builder /app/target/*.jar app.jar

# 设置启动脚本
ENTRYPOINT ["java", "-jar", "app.jar"]

# 暴露端口
EXPOSE 8080

# 健康检查
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD wget --no-verbose --tries=1 --spider http://localhost:8080/actuator/health || exit 1
