# 网关服务测试说明

## 测试概述

本项目的测试套件包含以下主要组件的测试：

### 1. GlobalExceptionHandler (全局异常处理器)
- **测试类**: `org.finger.handler.GlobalExceptionHandlerTest`
- **测试类型**: 单元测试
- **测试覆盖**:
  - ResponseStatusException 异常处理
  - TimeoutException 异常处理
  - ConnectException 异常处理
  - 通用异常处理
  - MDC追踪ID处理
  - JSON序列化异常处理
  - 空消息/null消息异常处理

### 2. LogFilter (日志过滤器)
- **测试类**: `org.finger.config.LogFilterTest`
- **测试类型**: 集成测试
- **测试覆盖**:
  - 成功请求日志流程
  - 失败请求异常日志流程
  - 追踪ID生成和传递
  - 客户端IP地址提取 (X-Forwarded-For, X-Real-IP, RemoteAddress)
  - 不同HTTP方法处理
  - 查询参数处理
  - 响应状态码处理
  - 并发请求隔离
  - User-Agent头处理
  - 请求处理时间计算

## 运行测试

### 方式一: 通过IDE运行
1. 在IDE中打开测试类
2. 右键点击测试类或测试方法
3. 选择 "Run"

### 方式二: 通过Maven运行特定测试类
```bash
# 运行全局异常处理器测试
mvn test -Dtest=GlobalExceptionHandlerTest

# 运行日志过滤器测试
mvn test -Dtest=LogFilterTest

# 运行所有测试
mvn test
```

### 方式三: 通过测试套件运行
```bash
# 运行TestRunner测试套件
mvn test -Dtest=TestRunner
```

## 测试报告

运行测试后，可以在以下位置查看测试报告：
- **控制台输出**: 实时测试结果
- **target/surefire-reports**: 详细的XML格式测试报告
- **target/site/jacoco**: 代码覆盖率报告（如果配置了JaCoCo）

## 测试配置

### Maven依赖
测试依赖已包含在 `pom.xml` 中：
- JUnit 5
- Mockito
- Reactor Test

### 测试配置
- 使用JUnit 5作为测试框架
- 使用Mockito进行Mock操作
- 使用Reactor Test进行响应式测试

## 测试最佳实践

1. **测试隔离**: 每个测试方法都是独立的，不依赖其他测试的状态
2. **MDC清理**: 每个测试前后都会清理MDC，确保测试环境干净
3. **Mock使用**: 合理使用Mock对象，避免不必要的依赖
4. **断言完整**: 验证关键行为和状态
5. **异常测试**: 覆盖正常和异常流程

## 添加新测试

如果要添加新的测试，请遵循以下规范：

1. **命名规范**: 测试类名以 `Test` 结尾，测试方法使用 `@DisplayName` 注解
2. **文档注释**: 为测试类和重要测试方法添加详细的中文注释
3. **测试结构**: 使用 Given-When-Then 模式组织测试代码
4. **断言清晰**: 使用有意义的断言，并提供清晰的错误消息

## 故障排除

### 常见问题

1. **测试失败**: 检查Mock配置是否正确
2. **端口冲突**: 确保测试使用的端口不冲突
3. **依赖问题**: 运行 `mvn clean install` 重新构建项目
4. **MDC问题**: 确保测试后清理MDC

### 调试技巧

1. 使用 `@Disabled` 暂时跳过有问题的测试
2. 添加日志输出帮助调试
3. 使用IDE的调试功能逐步执行测试
4. 检查测试报告中的详细信息

## 持续集成

这些测试设计为可以在CI/CD环境中自动运行：
- 无需外部依赖
- 执行时间短
- 结果稳定
- 提供清晰的失败信息
