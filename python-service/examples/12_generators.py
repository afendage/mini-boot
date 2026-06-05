#!/usr/bin/env python3
"""
案例 12: 生成器 (Generators)
知识点：
  - yield 关键字
  - 生成器函数
  - 生成器的优势 (内存高效)
  - send() 方法
  - 生成器的应用
"""

print("=" * 60)
print("案例 12: 生成器 (Generators)")
print("=" * 60)

# 【生成器基础】
print("\n【1. 生成器基础】")

# 普通函数返回列表
def get_numbers_list(n):
    """返回列表"""
    result = []
    for i in range(n):
        result.append(i)
    return result

# 生成器函数使用 yield
def get_numbers_generator(n):
    """生成器函数"""
    for i in range(n):
        yield i

print("列表方式:")
numbers_list = get_numbers_list(5)
print(f"  get_numbers_list(5) = {numbers_list}")
print(f"  类型: {type(numbers_list)}")

print("\\n生成器方式:")
numbers_gen = get_numbers_generator(5)
print(f"  get_numbers_generator(5) = {numbers_gen}")
print(f"  类型: {type(numbers_gen)}")

# 消耗生成器
print(f"\\n消耗生成器: {list(numbers_gen)}")

# 【生成器的延迟计算】
print("\n【2. 生成器的延迟计算】")

def countdown(n):
    """倒计时生成器"""
    print(f"  开始倒计时: {n}")
    while n > 0:
        yield n
        print(f"  产生了 {n}")
        n -= 1
    print("  倒计时完成!")

print("创建生成器 (未执行):")
gen = countdown(3)
print(f"  {gen}")

print("\\n通过 next() 逐个获取值:")
print(f"  next(gen) = {next(gen)}")
print(f"  next(gen) = {next(gen)}")
print(f"  next(gen) = {next(gen)}")

try:
    print(f"  next(gen) = {next(gen)}")
except StopIteration:
    print("  ❌ StopIteration: 生成器已耗尽")

# 【使用 for 循环遍历生成器】
print("\n【3. 使用 for 循环遍历生成器】")

def fibonacci(n):
    """生成前 n 个斐波那契数"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("遍历斐波那契生成器:")
for fib_num in fibonacci(10):
    print(f"  {fib_num}", end=" ")
print()

# 【生成器表达式】
print("\n【4. 生成器表达式】")

# 使用生成器表达式而不是列表推导式
print("列表推导式 (占用内存):")
large_list = [i ** 2 for i in range(5)]
print(f"  [i**2 for i in range(5)] = {large_list}")
print(f"  大小: {len(large_list)} 个元素")

print("\\n生成器表达式 (延迟计算):")
gen_expr = (i ** 2 for i in range(5))
print(f"  (i**2 for i in range(5)) = {gen_expr}")

print(f"  遍历:")
for value in gen_expr:
    print(f"    {value}", end=" ")
print()

# 【send() 方法】
print("\n【5. send() 方法】")

def echo():
    """可以接收值的生成器"""
    while True:
        value = yield  # 接收值，不返回任何东西
        if value is None:
            print("  接收到 None")
        else:
            print(f"  接收到: {value}")

print("使用 send() 方法:")
gen = echo()
next(gen)  # 初始化生成器，运行到第一个 yield

gen.send("Hello")
gen.send("World")
gen.send(None)

# 【生成器优势：内存效率】
print("\n【6. 生成器优势：内存效率】")

def read_large_file(lines):
    """模拟读取大文件"""
    print(f"  生成前 {lines} 行数据")
    for i in range(1, lines + 1):
        yield f"第 {i} 行数据"

print("使用生成器处理大文件:")
file_gen = read_large_file(1000000)
print(f"  生成器: {file_gen}")
print(f"  只消耗很少内存")

print("\\n只读取前 3 行:")
for i, line in enumerate(file_gen):
    if i < 3:
        print(f"    {line}")
    else:
        break

# 【生成器的链式操作】
print("\n【7. 生成器的链式操作】")

def numbers():
    """生成数字"""
    for i in range(1, 6):
        yield i

def square(numbers_gen):
    """平方"""
    for n in numbers_gen:
        yield n ** 2

def double(numbers_gen):
    """翻倍"""
    for n in numbers_gen:
        yield n * 2

print("链式操作: numbers() -> square() -> double():")
result = double(square(numbers()))
for value in result:
    print(f"  {value}", end=" ")
print()

# 【close() 和 throw() 方法】
print("\n【8. close() 和 throw() 方法】")

def generator_with_cleanup():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("  清理资源")

gen = generator_with_cleanup()
print(f"  next(gen) = {next(gen)}")
print(f"  next(gen) = {next(gen)}")
gen.close()
print("  已关闭生成器")

# 【实用案例】
print("\n【9. 实用案例】")

# 案例1: 无限生成器
print("\n案例1: 无限生成器")

def infinite_counter(start=0):
    """无限计数器生成器"""
    count = start
    while True:
        yield count
        count += 1

print("无限计数器 (前 5 个):")
counter = infinite_counter()
for i in range(5):
    print(f"  {next(counter)}", end=" ")
print()

# 案例2: 文件行读取生成器
print("\n案例2: 文件行读取生成器")

import os

def read_lines(filename):
    """逐行读取文件的生成器"""
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            yield line.rstrip('\\n')

# 创建测试文件
test_file = "d:\\work\\projects\\figer\\python-service\\sample_files\\lines.txt"
os.makedirs(os.path.dirname(test_file), exist_ok=True)
with open(test_file, 'w', encoding='utf-8') as f:
    f.write("第一行\\n第二行\\n第三行\\n")

print(f"读取 {test_file}:")
for i, line in enumerate(read_lines(test_file), 1):
    print(f"  {i}: {line}")

# 案例3: 数据过滤生成器
print("\n案例3: 数据过滤生成器")

def filter_gen(iterable, predicate):
    """根据条件过滤元素的生成器"""
    for item in iterable:
        if predicate(item):
            yield item

numbers = range(1, 11)
even_numbers = filter_gen(numbers, lambda x: x % 2 == 0)
print(f"偶数: {list(even_numbers)}")

# 案例4: 数据转换生成器
print("\n案例4: 数据转换生成器")

def map_gen(iterable, transform):
    """转换元素的生成器"""
    for item in iterable:
        yield transform(item)

numbers = [1, 2, 3, 4, 5]
squared = map_gen(numbers, lambda x: x ** 2)
print(f"平方: {list(squared)}")

# 案例5: 批处理生成器
print("\n案例5: 批处理生成器")

def batch(iterable, n):
    """将元素分批处理的生成器"""
    batch_list = []
    for item in iterable:
        batch_list.append(item)
        if len(batch_list) == n:
            yield batch_list
            batch_list = []
    if batch_list:
        yield batch_list

numbers = range(1, 11)
print("批大小为 3:")
for batch_data in batch(numbers, 3):
    print(f"  {batch_data}")

# 【性能对比】
print("\n【10. 性能对比】")

import sys

def memory_usage(obj):
    """获取对象的内存占用"""
    return sys.getsizeof(obj)

# 列表
list_obj = [i for i in range(1000)]
print(f"列表 (1000 个元素): {memory_usage(list_obj)} 字节")

# 生成器
gen_obj = (i for i in range(1000))
print(f"生成器 (1000 个元素): {memory_usage(gen_obj)} 字节")

print("\\n生成器优势:")
print("  1. 内存占用少")
print("  2. 处理大数据集效率高")
print("  3. 支持无限序列")
print("  4. 延迟计算避免不必要的计算")

print("\n✅ 生成器学习完成！\n")
