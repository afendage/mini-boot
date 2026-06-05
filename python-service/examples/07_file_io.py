#!/usr/bin/env python3
"""
案例 07: 文件 I/O 和异常处理
知识点：
  - 打开、读取、写入文件
  - with 语句 (上下文管理器)
  - 异常处理 (try/except/finally)
  - 常见异常类型
"""

import os

print("=" * 60)
print("案例 07: 文件 I/O 和异常处理")
print("=" * 60)

# 创建示例文件的目录
sample_dir = "d:\\work\\projects\\figer\\python-service\\sample_files"
if not os.path.exists(sample_dir):
    os.makedirs(sample_dir)

# 【文件的写入】
print("\n【1. 文件的写入】")

# 方法1: 不使用 with
print("方法1: 直接使用 open()")
file_path = os.path.join(sample_dir, "sample.txt")
f = open(file_path, "w", encoding="utf-8")
f.write("第一行\\n")
f.write("第二行\\n")
f.write("第三行\\n")
f.close()
print(f"  文件已写入: {file_path}")

# 方法2: 使用 with (推荐)
print("\\n方法2: 使用 with (推荐)")
file_path = os.path.join(sample_dir, "sample2.txt")
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Hello Python\\n")
    f.write("这是第二行\\n")
    f.write("这是第三行")
print(f"  文件已写入: {file_path}")

# 【文件的读取】
print("\n【2. 文件的读取】")

# 方法1: read() - 读取整个文件
print("\\nread() - 读取整个文件:")
file_path = os.path.join(sample_dir, "sample2.txt")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print(f"  文件内容:\\n{content}")

# 方法2: readline() - 读取一行
print("\\nreadline() - 读取一行:")
with open(file_path, "r", encoding="utf-8") as f:
    line1 = f.readline()
    line2 = f.readline()
    print(f"  第一行: {line1.strip()}")
    print(f"  第二行: {line2.strip()}")

# 方法3: readlines() - 读取所有行
print("\\nreadlines() - 读取所有行:")
with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"  共 {len(lines)} 行:")
    for i, line in enumerate(lines, 1):
        print(f"    {i}: {line.strip()}")

# 方法4: 循环遍历
print("\\n循环遍历文件:")
with open(file_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"    {i}: {line.strip()}")

# 【文件的附加】
print("\n【3. 文件的附加 (append)】")
file_path = os.path.join(sample_dir, "sample2.txt")
with open(file_path, "a", encoding="utf-8") as f:
    f.write("\\n附加的第四行\\n")
    f.write("附加的第五行")
print("  内容已附加")

# 读取验证
with open(file_path, "r", encoding="utf-8") as f:
    print("  更新后的文件内容:")
    for line in f:
        print(f"    {line.rstrip()}")

# 【异常处理】
print("\n【4. 异常处理】")

# try/except
print("\\ntry/except - 处理异常:")
try:
    x = 10
    y = 0
    result = x / y
except ZeroDivisionError:
    print("  ❌ 错误: 不能除以 0")
except Exception as e:
    print(f"  ❌ 发生异常: {type(e).__name__}: {e}")

# try/except/else
print("\\ntry/except/else:")
try:
    x = 10
    y = 2
    result = x / y
except ZeroDivisionError:
    print("  ❌ 错误: 不能除以 0")
else:
    print(f"  ✅ 计算成功: {x} / {y} = {result}")

# try/except/finally
print("\\ntry/except/finally:")
file_path = os.path.join(sample_dir, "test.txt")
try:
    f = open(file_path, "r", encoding="utf-8")
    content = f.read()
    print(f"  ✅ 文件读取成功")
except FileNotFoundError:
    print(f"  ❌ 错误: 文件不存在")
finally:
    if 'f' in locals() and not f.closed:
        f.close()
    print("  ✅ 清理工作完成")

# try/except/else/finally
print("\\ntry/except/else/finally:")
try:
    numbers = [1, 2, 3]
    print(f"  列表: {numbers}")
    num = numbers[1]
except IndexError:
    print("  ❌ 错误: 索引超出范围")
else:
    print(f"  ✅ 成功获取元素: {num}")
finally:
    print("  ✅ 处理完成")

# 【常见异常类型】
print("\n【5. 常见异常类型】")

exceptions = [
    ("ZeroDivisionError", lambda: 10 / 0),
    ("ValueError", lambda: int("abc")),
    ("IndexError", lambda: [][0]),
    ("KeyError", lambda: {}["key"]),
    ("TypeError", lambda: "a" + 1),
    ("AttributeError", lambda: "".nonexistent_method()),
    ("NameError", lambda: undefined_variable),
]

for exc_name, exc_func in exceptions:
    try:
        exc_func()
    except Exception as e:
        print(f"  {exc_name}: {e}")

# 【自定义异常】
print("\n【6. 自定义异常】")

class CustomError(Exception):
    """自定义异常"""
    pass

class NegativeNumberError(Exception):
    """负数异常"""
    pass

def check_age(age):
    if age < 0:
        raise NegativeNumberError("年龄不能为负数")
    elif age < 18:
        raise ValueError("年龄必须大于等于 18")
    return "成年人"

print("测试自定义异常:")
test_ages = [25, -5, 15]
for age in test_ages:
    try:
        result = check_age(age)
        print(f"  年龄 {age}: ✅ {result}")
    except NegativeNumberError as e:
        print(f"  年龄 {age}: ❌ {type(e).__name__}: {e}")
    except ValueError as e:
        print(f"  年龄 {age}: ❌ {type(e).__name__}: {e}")

# 【异常的重新抛出】
print("\n【7. 异常的重新抛出】")

def process_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"  ❌ 文件不存在: {filename}")
        raise  # 重新抛出异常

try:
    content = process_file("nonexistent.txt")
except FileNotFoundError:
    print("  捕获到重新抛出的异常")

# 【实用案例】
print("\n【8. 实用案例】")

# 案例1: 安全地读取配置文件
print("\\n案例1: 安全地读取配置文件")
def read_config(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            config = {}
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    try:
                        key, value = line.split("=")
                        config[key.strip()] = value.strip()
                    except ValueError:
                        print(f"  ⚠️ 配置行格式错误: {line}")
            return config
    except FileNotFoundError:
        print(f"  ❌ 配置文件不存在: {filename}")
        return {}

# 创建配置文件
config_file = os.path.join(sample_dir, "config.txt")
with open(config_file, "w", encoding="utf-8") as f:
    f.write("# 这是配置文件\\n")
    f.write("host=localhost\\n")
    f.write("port=8080\\n")
    f.write("debug=true\\n")
    f.write("invalid line without equals\\n")

config = read_config(config_file)
print("  读取的配置:")
for key, value in config.items():
    print(f"    {key} = {value}")

# 案例2: 文件转换 (CSV 到字典)
print("\\n案例2: 转换 CSV 到字典列表")
csv_file = os.path.join(sample_dir, "data.csv")
with open(csv_file, "w", encoding="utf-8") as f:
    f.write("姓名,年龄,城市\\n")
    f.write("张三,25,北京\\n")
    f.write("李四,30,上海\\n")
    f.write("王五,28,广州\\n")

def read_csv(filename):
    data = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            header = f.readline().strip().split(",")
            for line in f:
                values = line.strip().split(",")
                if len(values) == len(header):
                    data.append(dict(zip(header, values)))
    except FileNotFoundError:
        print(f"  ❌ 文件不存在: {filename}")
    return data

data = read_csv(csv_file)
print("  CSV 数据:")
for row in data:
    print(f"    {row}")

print("\\n✅ 文件 I/O 和异常处理学习完成！\\n")
