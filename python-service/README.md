# Python 示例服务

这是一个简单的 Python Flask 服务示例，包含常见基础用例。

## 目录

- `app.py` - Flask 应用程序入口
- `requirements.txt` - 依赖列表

## 快速启动

1. 创建并激活虚拟环境：
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
3. 运行服务：
   ```bash
   python app.py
   ```

服务默认监听 `http://127.0.0.1:5000`。

## 示例接口

- `GET /` - 服务首页，返回可用接口列表
- `GET /health` - 健康检查
- `GET /examples/basic` - 返回基础 JSON 示例
- `GET /examples/echo?text=hello` - 读取查询参数并回显
- `POST /examples/sum` - 计算 JSON body 中 `numbers` 列表的和
- `GET /examples/user/<username>` - 演示路径参数

## 请求示例

### echo

```bash
curl "http://127.0.0.1:5000/examples/echo?text=hello"
```

### sum

```bash
curl -X POST http://127.0.0.1:5000/examples/sum \
  -H "Content-Type: application/json" \
  -d '{"numbers": [1, 2, 3, 4]}'
```

### user

```bash
curl http://127.0.0.1:5000/examples/user/zhangsan
```
