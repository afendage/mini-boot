#!/usr/bin/env python3
"""
案例 13: JSON 处理
知识点：
  - JSON 基本格式
  - json.dumps() - Python 对象转 JSON 字符串
  - json.loads() - JSON 字符串转 Python 对象
  - json.dump() - Python 对象保存到文件
  - json.load() - 从文件加载 JSON
  - 处理复杂对象
"""

import json
import os
from datetime import datetime

print("=" * 60)
print("案例 13: JSON 处理")
print("=" * 60)

# 创建输出目录
output_dir = "d:\\work\\projects\\figer\\python-service\\sample_files"
os.makedirs(output_dir, exist_ok=True)

# 【JSON 基本概念】
print("\n【1. JSON 基本概念】")

print("JSON 是一种轻量级的数据交换格式")
print("\\nJSON 数据类型:")
print("  - 字符串: \\\"hello\\\"")
print("  - 数字: 123, 45.67")
print("  - 布尔值: true, false")
print("  - null: null")
print("  - 对象: {\\\"key\\\": \\\"value\\\"}")
print("  - 数组: [1, 2, 3]")

# 【json.dumps() - Python 对象转 JSON 字符串】
print("\n【2. json.dumps() - Python 对象转 JSON 字符串】")

# 基本类型转换
data = {
    "name": "张三",
    "age": 25,
    "is_student": False,
    "hobbies": ["读书", "游泳", "编程"],
    "scores": {"语文": 90, "数学": 95, "英文": 88},
    "nothing": None
}

print("Python 对象:")
print(f"  {data}")

# 转为 JSON 字符串
json_str = json.dumps(data, ensure_ascii=False)
print(f"\\njson.dumps() 结果 (紧凑):")
print(f"  {json_str}")

# 带缩进的 JSON (便于阅读)
json_str_pretty = json.dumps(data, ensure_ascii=False, indent=2)
print(f"\\njson.dumps() 结果 (缩进):")
print(json_str_pretty)

# 排序键
json_str_sorted = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)
print(f"\\njson.dumps() 结果 (排序键):")
print(json_str_sorted)

# 【json.loads() - JSON 字符串转 Python 对象】
print("\n【3. json.loads() - JSON 字符串转 Python 对象】")

json_str = '{"name": "李四", "age": 30, "city": "上海"}'
print(f"JSON 字符串: {json_str}")

python_obj = json.loads(json_str)
print(f"\\njson.loads() 结果:")
print(f"  类型: {type(python_obj)}")
print(f"  内容: {python_obj}")
print(f"  访问: name={python_obj['name']}, age={python_obj['age']}")

# 【json.dump() - 保存到文件】
print("\n【4. json.dump() - 保存到文件】")

students = [
    {"name": "张三", "age": 22, "major": "计算机科学"},
    {"name": "李四", "age": 23, "major": "软件工程"},
    {"name": "王五", "age": 21, "major": "数据科学"}
]

file_path = os.path.join(output_dir, "students.json")

# 保存到文件
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

print(f"数据已保存到: {file_path}")

# 读取文件显示
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
    print("\\n文件内容:")
    print(content)

# 【json.load() - 从文件加载】
print("\n【5. json.load() - 从文件加载】")

with open(file_path, 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

print(f"加载的数据类型: {type(loaded_data)}")
print(f"加载的数据:")
for student in loaded_data:
    print(f"  {student['name']}: {student['major']}")

# 【处理不同的数据类型】
print("\n【6. 处理不同的数据类型】")

# 数字
print("数字:")
print(f"  {json.dumps(123)}")
print(f"  {json.dumps(45.67)}")

# 布尔值
print("\\n布尔值:")
print(f"  {json.dumps(True)}")
print(f"  {json.dumps(False)}")

# None
print("\\nNone:")
print(f"  {json.dumps(None)}")

# 列表
print("\\n列表:")
print(f"  {json.dumps([1, 'hello', 3.14, True, None])}")

# 嵌套结构
print("\\n嵌套结构:")
nested = {
    "users": [
        {"id": 1, "name": "Alice", "posts": [1, 2, 3]},
        {"id": 2, "name": "Bob", "posts": [4, 5]}
    ]
}
print(json.dumps(nested, indent=2))

# 【处理日期时间】
print("\n【7. 处理日期时间】")

# 日期时间不能直接序列化
data_with_datetime = {
    "name": "张三",
    "created_at": datetime.now()
}

print("尝试直接序列化包含 datetime 的对象:")
try:
    json.dumps(data_with_datetime)
except TypeError as e:
    print(f"  ❌ {e}")

# 解决方案1: 转为字符串
print("\\n解决方案1: 转为字符串")
data_fixed = {
    "name": "张三",
    "created_at": datetime.now().isoformat()
}
print(f"  {json.dumps(data_fixed, ensure_ascii=False)}")

# 解决方案2: 自定义 JSONEncoder
print("\\n解决方案2: 自定义 JSONEncoder")

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

data_with_datetime = {
    "name": "张三",
    "created_at": datetime.now()
}
print(f"  {json.dumps(data_with_datetime, cls=DateTimeEncoder, ensure_ascii=False)}")

# 【处理自定义对象】
print("\n【8. 处理自定义对象】")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 方法1: 定义 __dict__
person = Person("李四", 25)
print(f"使用 __dict__: {json.dumps(person.__dict__)}")

# 方法2: 自定义序列化函数
def custom_encoder(obj):
    if isinstance(obj, Person):
        return {"name": obj.name, "age": obj.age}
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

print(f"自定义函数: {json.dumps(person, default=custom_encoder)}")

# 【实用案例】
print("\n【9. 实用案例】")

# 案例1: API 响应处理
print("\n案例1: 模拟 API 响应处理")

api_response = '''
{
    "status": "success",
    "code": 200,
    "data": {
        "user": {
            "id": 123,
            "name": "张三",
            "email": "zhangsan@example.com"
        },
        "posts": [
            {"id": 1, "title": "Python 基础", "likes": 10},
            {"id": 2, "title": "Web 开发", "likes": 25}
        ]
    }
}
'''

response = json.loads(api_response)
print(f"API 状态: {response['status']} (代码: {response['code']})")
print(f"用户名: {response['data']['user']['name']}")
print(f"用户邮箱: {response['data']['user']['email']}")
print(f"\\n用户文章:")
for post in response['data']['posts']:
    print(f"  - {post['title']} ({post['likes']} 赞)")

# 案例2: 配置文件处理
print("\n案例2: 配置文件处理")

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "username": "admin",
        "password": "secret"
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8080,
        "debug": True
    },
    "logging": {
        "level": "INFO",
        "file": "app.log"
    }
}

config_file = os.path.join(output_dir, "config.json")
with open(config_file, 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2)

print(f"配置已保存到: {config_file}")

# 读取配置
with open(config_file, 'r', encoding='utf-8') as f:
    loaded_config = json.load(f)

print(f"\\n数据库配置:")
print(f"  主机: {loaded_config['database']['host']}")
print(f"  端口: {loaded_config['database']['port']}")

print(f"\\n服务器配置:")
print(f"  主机: {loaded_config['server']['host']}")
print(f"  端口: {loaded_config['server']['port']}")

# 案例3: 数据验证
print("\n案例3: 数据验证和错误处理")

def validate_json(json_str):
    """验证 JSON 字符串的有效性"""
    try:
        data = json.loads(json_str)
        print(f"  ✅ 有效的 JSON")
        return data
    except json.JSONDecodeError as e:
        print(f"  ❌ 无效的 JSON: {e}")
        return None

print("测试有效的 JSON:")
validate_json('{"name": "Alice", "age": 30}')

print("\\n测试无效的 JSON:")
validate_json('{"name": "Bob", "age": 30')  # 缺少结束括号

# 案例4: 数据格式化输出
print("\n案例4: 数据格式化输出")

class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

records = [
    Record(id=1, name="商品 A", price=99.99, stock=50),
    Record(id=2, name="商品 B", price=149.99, stock=30),
    Record(id=3, name="商品 C", price=49.99, stock=0)
]

records_data = [r.__dict__ for r in records]
output_file = os.path.join(output_dir, "products.json")

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(records_data, f, ensure_ascii=False, indent=2)

print(f"商品数据已保存到: {output_file}")

# 读取并显示
with open(output_file, 'r', encoding='utf-8') as f:
    products = json.load(f)
    for p in products:
        stock_status = "有货" if p['stock'] > 0 else "缺货"
        print(f"  {p['name']}: ¥{p['price']} ({stock_status})")

print("\n✅ JSON 处理学习完成！\n")
