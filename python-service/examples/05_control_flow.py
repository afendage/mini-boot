#!/usr/bin/env python3
"""
案例 05: 控制流 (if/else/for/while)
知识点：
  - if/elif/else 条件语句
  - for 循环
  - while 循环
  - break, continue, pass
  - 循环中的 else 子句
"""

print("=" * 60)
print("案例 05: 控制流 (if/else/for/while)")
print("=" * 60)

# 【if/elif/else 条件语句】
print("\n【1. if/elif/else 条件语句】")

# 简单的 if
print("\n简单的 if:")
age = 20
if age >= 18:
    print("你是成年人")

# if/else
print("\nif/else:")
age = 15
if age >= 18:
    print("你是成年人")
else:
    print("你是未成年人")

# if/elif/else
print("\nif/elif/else:")
score = 85
if score >= 90:
    print("成绩: A")
elif score >= 80:
    print("成绩: B")
elif score >= 70:
    print("成绩: C")
else:
    print("成绩: F")

# 嵌套 if
print("\n嵌套 if:")
age = 25
is_student = False
if age >= 18:
    if is_student:
        print("你是大学生")
    else:
        print("你是成年人，但不是学生")
else:
    print("你未成年")

# 条件表达式 (三元运算符)
print("\n条件表达式 (三元运算符):")
age = 20
status = "成年人" if age >= 18 else "未成年人"
print(f"年龄 {age}: {status}")

# 逻辑运算符
print("\n逻辑运算符:")
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"年龄 {age}, 有驾照: {has_license}")
print(f"可以开车: {can_drive}")

# 【for 循环】
print("\n【2. for 循环】")

# 遍历列表
print("\n遍历列表:")
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"  {fruit}")

# 使用 range()
print("\nrange() 循环:")
for i in range(5):
    print(f"  {i}", end=" ")
print()

print("\nrange(2, 8):")
for i in range(2, 8):
    print(f"  {i}", end=" ")
print()

print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(f"  {i}", end=" ")
print()

# enumerate() - 获取索引和值
print("\nenumerate() - 获取索引和值:")
fruits = ["苹果", "香蕉", "橙子"]
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# 遍历字典
print("\n遍历字典:")
person = {"name": "张三", "age": 25, "city": "北京"}
for key, value in person.items():
    print(f"  {key}: {value}")

# zip() - 并行遍历
print("\nzip() - 并行遍历:")
names = ["张三", "李四", "王五"]
ages = [25, 30, 28]
for name, age in zip(names, ages):
    print(f"  {name}: {age}岁")

# 【while 循环】
print("\n【3. while 循环】")

print("\n简单的 while:")
count = 0
while count < 3:
    print(f"  count = {count}")
    count += 1

# 猜数字游戏
print("\n猜数字游戏 (模拟):")
secret = 5
guess = 0
attempts = 0
while guess != secret:
    guess = (attempts + 1) * 2  # 模拟猜数字
    attempts += 1
    if guess < secret:
        print(f"  第 {attempts} 次: 猜测 {guess}, 太小了")
    elif guess > secret:
        print(f"  第 {attempts} 次: 猜测 {guess}, 太大了")

# 【break 和 continue】
print("\n【4. break 和 continue】")

print("\nbreak - 跳出循环:")
for i in range(10):
    if i == 5:
        print(f"  在 i={i} 时停止")
        break
    print(f"  {i}", end=" ")
print()

print("\ncontinue - 跳过当前迭代:")
for i in range(5):
    if i == 2:
        print(f"  跳过 {i}")
        continue
    print(f"  {i}", end=" ")
print()

# 【pass 语句】
print("\n【5. pass 语句】")
print("pass 用于占位符:")
for i in range(3):
    if i == 1:
        pass  # 什么都不做
    else:
        print(f"  {i}")

# 【for/else 循环】
print("\n【6. for/else 循环】")

# 没有 break 的情况
print("\n没有 break 的情况:")
for i in range(3):
    print(f"  循环: {i}")
else:
    print("  循环正常完成")

# 有 break 的情况
print("\n有 break 的情况:")
for i in range(5):
    if i == 3:
        print(f"  在 i={i} 时 break")
        break
    print(f"  循环: {i}")
else:
    print("  循环正常完成")  # 这行不会执行

# 【while/else 循环】
print("\n【7. while/else 循环】")

print("\nwhile 正常完成:")
count = 0
while count < 3:
    print(f"  count = {count}")
    count += 1
else:
    print("  while 正常完成")

# 【实用案例】
print("\n【8. 实用案例】")

# 案例1: 九九乘法表
print("\n案例1: 九九乘法表")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i*j}", end="  ")
    print()

# 案例2: 找出列表中最大值
print("\n案例2: 找出列表中最大值")
numbers = [45, 23, 67, 89, 12, 34]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"列表: {numbers}")
print(f"最大值: {max_num}")

# 案例3: 判断素数
print("\n案例3: 判断素数")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

test_numbers = [2, 3, 4, 5, 10, 17, 20]
for num in test_numbers:
    if is_prime(num):
        print(f"  {num} 是素数")
    else:
        print(f"  {num} 不是素数")

# 案例4: 统计字符出现次数
print("\n案例4: 统计字符出现次数")
text = "hello world"
char_count = {}
for char in text:
    if char != ' ':
        char_count[char] = char_count.get(char, 0) + 1

print(f"文本: '{text}'")
for char, count in sorted(char_count.items()):
    print(f"  '{char}': {count}次")

print("\n✅ 控制流学习完成！\n")
