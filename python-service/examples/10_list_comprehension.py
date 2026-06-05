#!/usr/bin/env python3
"""
案例 10: 列表推导式、字典推导式和集合推导式
知识点：
  - 列表推导式 (List Comprehension)
  - 字典推导式 (Dict Comprehension)
  - 集合推导式 (Set Comprehension)
  - 生成器表达式
"""

print("=" * 60)
print("案例 10: 列表推导式和推导式")
print("=" * 60)

# 【列表推导式基础】
print("\n【1. 列表推导式基础】")

# 传统方式
print("传统方式:")
numbers = []
for i in range(1, 6):
    numbers.append(i ** 2)
print(f"  {numbers}")

# 列表推导式
print("\\n列表推导式:")
numbers = [i ** 2 for i in range(1, 6)]
print(f"  [i**2 for i in range(1, 6)] = {numbers}")

# 【列表推导式高级用法】
print("\n【2. 列表推导式高级用法】")

# 带条件的列表推导式
print("带条件的列表推导式:")
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(f"  [i for i in range(1, 11) if i % 2 == 0] = {even_numbers}")

odd_numbers = [i for i in range(1, 11) if i % 2 != 0]
print(f"  [i for i in range(1, 11) if i % 2 != 0] = {odd_numbers}")

# 嵌套列表推导式
print("\\n嵌套列表推导式:")
matrix = [[i + j for j in range(1, 4)] for i in range(0, 9, 3)]
print(f"  矩阵: {matrix}")

# 字符串处理
print("\\n字符串处理:")
text = "hello world"
uppercase = [char.upper() for char in text if char != ' ']
print(f"  [char.upper() for char in 'hello world' if char != ' ']")
print(f"  {uppercase}")

# 列表扁平化
print("\\n列表扁平化:")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(f"  原矩阵: {matrix}")
print(f"  扁平化: {flat}")

# 条件表达式
print("\\n条件表达式:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = ["偶数" if i % 2 == 0 else "奇数" for i in numbers]
print(f"  {result}")

# 【字典推导式】
print("\n【3. 字典推导式】")

# 基础字典推导式
print("基础字典推导式:")
squares = {i: i ** 2 for i in range(1, 6)}
print(f"  {{i: i**2 for i in range(1, 6)}} = {squares}")

# 从列表创建字典
print("\\n从列表创建字典:")
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
d = {k: v for k, v in zip(keys, values)}
print(f"  {{k: v for k, v in zip({keys}, {values})}} = {d}")

# 字典反转
print("\\n字典反转:")
original = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in original.items()}
print(f"  原字典: {original}")
print(f"  反转: {reversed_dict}")

# 字符串频率统计
print("\\n字符频率统计:")
text = "programming"
freq = {char: text.count(char) for char in set(text)}
print(f"  文本: '{text}'")
print(f"  频率: {sorted(freq.items())}")

# 条件字典推导式
print("\\n条件字典推导式:")
numbers = range(1, 11)
even_squares = {i: i ** 2 for i in numbers if i % 2 == 0}
print(f"  {{i: i**2 for i in range(1, 11) if i % 2 == 0}} = {even_squares}")

# 【集合推导式】
print("\n【4. 集合推导式】")

# 基础集合推导式
print("基础集合推导式:")
squares = {i ** 2 for i in range(1, 6)}
print(f"  {{i**2 for i in range(1, 6)}} = {squares}")

# 去重
print("\\n去重:")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {i for i in numbers}
print(f"  原列表: {numbers}")
print(f"  去重后: {unique}")

# 条件集合推导式
print("\\n条件集合推导式:")
text = "hello world"
vowels = {char for char in text if char in 'aeiou'}
print(f"  {{char for char in 'hello world' if char in 'aeiou'}} = {vowels}")

# 【生成器表达式】
print("\n【5. 生成器表达式】")

# 列表推导式 vs 生成器表达式
print("列表推导式 (占用内存):")
list_comp = [i for i in range(5)]
print(f"  [i for i in range(5)] = {list_comp}")
print(f"  类型: {type(list_comp)}")

print("\\n生成器表达式 (延迟计算):")
gen_exp = (i for i in range(5))
print(f"  (i for i in range(5)) = {gen_exp}")
print(f"  类型: {type(gen_exp)}")

print("\\n消耗生成器:")
for i in (i for i in range(5)):
    print(f"  {i}", end=" ")
print()

# 生成器与 sum, max, min
print("\\n生成器与内置函数:")
numbers_gen = (i for i in range(1, 6))
print(f"  sum((i for i in range(1, 6))) = {sum(numbers_gen)}")

numbers_gen = (i for i in range(1, 6))
print(f"  max((i for i in range(1, 6))) = {max(numbers_gen)}")

# 【实用案例】
print("\n【6. 实用案例】")

# 案例1: 处理学生成绩
print("\n案例1: 处理学生成绩")
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
    {"name": "赵六", "score": 88},
    {"name": "孙七", "score": 95},
]

# 获取所有成绩
scores = [s["score"] for s in students]
print(f"  所有成绩: {scores}")

# 筛选及格的学生
passed = [s for s in students if s["score"] >= 80]
print(f"  及格的学生: {[s['name'] for s in passed]}")

# 创建成绩字典
scores_dict = {s["name"]: s["score"] for s in students}
print(f"  成绩字典: {scores_dict}")

# 统计及格人数
pass_count = len([s for s in students if s["score"] >= 80])
print(f"  及格人数: {pass_count}")

# 案例2: 数据转换
print("\\n案例2: 数据转换")
raw_data = "1,2,3,4,5,6,7,8,9,10"

# 转为整数列表
numbers = [int(x) for x in raw_data.split(',')]
print(f"  原数据: {raw_data}")
print(f"  整数列表: {numbers}")

# 计算平方
squares = [n ** 2 for n in numbers]
print(f"  平方: {squares}")

# 筛选大于 5 的数
filtered = [n for n in numbers if n > 5]
print(f"  > 5 的数: {filtered}")

# 案例3: 文件名处理
print("\\n案例3: 文件名处理")
filenames = ["image1.jpg", "document.pdf", "photo.png", "file.doc", "picture.jpg"]

# 获取所有 jpg 文件
jpg_files = [f for f in filenames if f.endswith('.jpg')]
print(f"  jpg 文件: {jpg_files}")

# 提取文件名 (不含扩展名)
names = [f.split('.')[0] for f in filenames]
print(f"  文件名: {names}")

# 统计每种文件类型
extensions = set(f.split('.')[1] for f in filenames)
print(f"  文件类型: {extensions}")

# 案例4: 复杂的嵌套推导式
print("\\n案例4: 复杂的嵌套推导式")
# 生成乘法表
multiplication_table = {
    f"{i}*{j}": i * j 
    for i in range(1, 6) 
    for j in range(1, 6)
}
print(f"  前几个乘法结果: {dict(list(multiplication_table.items())[:5])}")

# 【性能对比】
print("\n【7. 性能对比 (概念)】")

# 列表推导式通常比循环更快、更简洁
print("列表推导式优点:")
print("  1. 代码更简洁")
print("  2. 性能更高")
print("  3. 可读性强 (对于简单操作)")

print("\\n生成器表达式优点:")
print("  1. 内存高效 (延迟计算)")
print("  2. 适合处理大数据")
print("  3. 可与管道操作结合")

print("\n✅ 列表推导式和推导式学习完成！\n")
