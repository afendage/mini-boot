#!/usr/bin/env python3
"""
案例 06: 函数 (Functions)
知识点：
  - 函数的定义和调用
  - 参数: 位置参数、默认参数、可变参数 (*args, **kwargs)
  - 返回值
  - 作用域和命名空间
  - 匿名函数 (lambda)
"""

print("=" * 60)
print("案例 06: 函数 (Functions)")
print("=" * 60)

# 【函数的定义和调用】
print("\n【1. 函数的定义和调用】")

def greet():
    """这是一个问候函数"""
    print("  你好，欢迎来到 Python!")

print("调用 greet():")
greet()

# 【函数的参数】
print("\n【2. 函数的参数】")

# 位置参数
def add(a, b):
    """计算两个数的和"""
    return a + b

print(f"add(3, 5) = {add(3, 5)}")

# 默认参数
def greet_person(name, greeting="你好"):
    """带默认参数的问候函数"""
    print(f"  {greeting}, {name}!")

print("调用 greet_person():")
greet_person("张三")
greet_person("李四", "早安")

# 关键字参数
def describe_person(name, age, city):
    """描述一个人"""
    print(f"  名字: {name}, 年龄: {age}, 城市: {city}")

print("\n关键字参数:")
describe_person(name="王五", age=25, city="北京")
describe_person(age=30, city="上海", name="赵六")

# 【可变参数】
print("\n【3. 可变参数】")

# *args - 接收任意数量的位置参数 (元组)
def sum_all(*numbers):
    """计算所有参数的和"""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# **kwargs - 接收任意数量的关键字参数 (字典)
def print_info(**info):
    """打印任意数量的键值对"""
    for key, value in info.items():
        print(f"  {key}: {value}")

print("\nprint_info():")
print_info(name="张三", age=25, city="北京", job="工程师")

# 结合 *args 和 **kwargs
def print_all(arg1, *args, **kwargs):
    """同时处理位置参数、可变参数和关键字参数"""
    print(f"  第一个参数: {arg1}")
    print(f"  其他位置参数: {args}")
    print(f"  关键字参数: {kwargs}")

print("\nprint_all():")
print_all("第一个", "第二个", "第三个", name="张三", age=25)

# 【返回值】
print("\n【4. 返回值】")

# 单个返回值
def square(x):
    return x * x

print(f"square(5) = {square(5)}")

# 多个返回值
def divide_and_remainder(a, b):
    """返回商和余数"""
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_and_remainder(17, 5)
print(f"divide_and_remainder(17, 5) = ({q}, {r})")

# 【函数的文档字符串】
print("\n【5. 函数的文档字符串】")

def calculate_bmi(weight, height):
    """
    计算体重指数 (BMI)
    
    参数:
        weight: 体重 (kg)
        height: 身高 (m)
    
    返回:
        BMI 值
    """
    return weight / (height ** 2)

print(f"BMI = {calculate_bmi(70, 1.75):.2f}")
print(f"函数文档: {calculate_bmi.__doc__}")

# 【作用域】
print("\n【6. 作用域 (Scope)】")

global_var = "全局变量"

def outer():
    outer_var = "外层变量"
    
    def inner():
        inner_var = "内层变量"
        print(f"  inner_var: {inner_var}")
        print(f"  outer_var: {outer_var}")
        print(f"  global_var: {global_var}")
    
    inner()

print("函数嵌套和作用域:")
outer()

# 修改全局变量
print("\n修改全局变量:")
counter = 0

def increment():
    global counter
    counter += 1
    return counter

print(f"increment() = {increment()}")
print(f"increment() = {increment()}")
print(f"increment() = {increment()}")

# 【lambda 函数 (匿名函数)】
print("\n【7. lambda 函数 (匿名函数)】")

# 简单的 lambda
square = lambda x: x * x
print(f"lambda x: x * x")
print(f"  square(5) = {square(5)}")

# 多个参数的 lambda
add = lambda x, y: x + y
print(f"lambda x, y: x + y")
print(f"  add(3, 4) = {add(3, 4)}")

# lambda 常与高阶函数一起使用
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"\nmap(lambda x: x ** 2, {numbers})")
print(f"  结果: {squared}")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nfilter(lambda x: x % 2 == 0, {numbers})")
print(f"  结果: {even_numbers}")

# 【高阶函数】
print("\n【8. 高阶函数】")

def apply_operation(x, y, operation):
    """对两个数执行指定的操作"""
    return operation(x, y)

print(f"apply_operation(5, 3, lambda x, y: x + y) = {apply_operation(5, 3, lambda x, y: x + y)}")
print(f"apply_operation(5, 3, lambda x, y: x * y) = {apply_operation(5, 3, lambda x, y: x * y)}")

# 【实用案例】
print("\n【9. 实用案例】")

# 案例1: 计算阶乘
print("\n案例1: 计算阶乘")
def factorial(n):
    """计算 n 的阶乘"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

for i in range(1, 6):
    print(f"  {i}! = {factorial(i)}")

# 案例2: 斐波那契数列
print("\n案例2: 斐波那契数列")
def fibonacci(n):
    """返回前 n 个斐波那契数"""
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    
    fib_list = [1, 1]
    for i in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

print(f"  前 10 个斐波那契数: {fibonacci(10)}")

# 案例3: 过滤和排序
print("\n案例3: 过滤和排序")
students = [
    {"name": "张三", "score": 85},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 78},
    {"name": "赵六", "score": 88},
]

# 筛选成绩大于 80 的学生
good_students = list(filter(lambda s: s["score"] > 80, students))
print(f"  成绩 > 80 的学生:")
for student in good_students:
    print(f"    {student['name']}: {student['score']}")

# 按成绩排序
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)
print(f"  按成绩排序:")
for student in sorted_students:
    print(f"    {student['name']}: {student['score']}")

print("\n✅ 函数学习完成！\n")
