#!/usr/bin/env python3
"""
案例 01: 变量和数据类型
知识点：
  - 变量的定义和赋值
  - Python 的基本数据类型: int, float, str, bool
  - 类型转换
  - 类型检查 (type())
"""

print("=" * 60)
print("案例 01: 变量和数据类型")
print("=" * 60)

# 【整数类型】
print("\n【1. 整数类型 (int)】")
age = 25
count = 100
negative = -50
print(f"age = {age}, 类型: {type(age)}")
print(f"count = {count}, 类型: {type(count)}")
print(f"negative = {negative}, 类型: {type(negative)}")

# 整数运算
print("\n【整数运算】")
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")  # 结果是浮点数
print(f"{a} // {b} = {a // b}")  # 整数除法
print(f"{a} % {b} = {a % b}")  # 取余
print(f"{a} ** {b} = {a ** b}")  # 幂运算

# 【浮点数类型】
print("\n【2. 浮点数类型 (float)】")
height = 1.75
price = 99.99
pi = 3.14159
print(f"height = {height}, 类型: {type(height)}")
print(f"price = {price}, 类型: {type(price)}")
print(f"pi = {pi}, 类型: {type(pi)}")

# 浮点数运算
print("\n【浮点数运算】")
x = 2.5
y = 1.2
print(f"{x} + {y} = {x + y}")
print(f"{x} * {y} = {x * y}")
print(f"round({x}, 1) = {round(x, 1)}")  # 四舍五入

# 【字符串类型】
print("\n【3. 字符串类型 (str)】")
name = "Python"
message = "Hello World"
empty_str = ""
print(f"name = '{name}', 类型: {type(name)}")
print(f"message = '{message}', 类型: {type(message)}")
print(f"empty_str = '{empty_str}', 长度: {len(empty_str)}")

# 字符串操作
print("\n【字符串操作】")
str1 = "Hello"
str2 = "Python"
print(f"'{str1}' + '{str2}' = '{str1 + str2}'")  # 字符串连接
print(f"'{str1}' * 3 = '{str1 * 3}'")  # 字符串重复
print(f"len('{str1}') = {len(str1)}")  # 字符串长度
print(f"'{str1}'[0] = '{str1[0]}'")  # 获取第一个字符
print(f"'{str1}'[-1] = '{str1[-1]}'")  # 获取最后一个字符
print(f"'{str1}'.upper() = '{str1.upper()}'")  # 转大写
print(f"'{str1}'.lower() = '{str1.lower()}'")  # 转小写

# 【布尔类型】
print("\n【4. 布尔类型 (bool)】")
is_student = True
is_adult = False
print(f"is_student = {is_student}, 类型: {type(is_student)}")
print(f"is_adult = {is_adult}, 类型: {type(is_adult)}")

# 布尔运算
print("\n【布尔运算】")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# 【类型转换】
print("\n【5. 类型转换】")
# 转为整数
print(f"int('123') = {int('123')}")
print(f"int(45.99) = {int(45.99)}")  # 截断小数部分
print(f"int(True) = {int(True)}")

# 转为浮点数
print(f"float('3.14') = {float('3.14')}")
print(f"float(10) = {float(10)}")

# 转为字符串
print(f"str(123) = '{str(123)}'")
print(f"str(3.14) = '{str(3.14)}'")
print(f"str(True) = '{str(True)}'")

# 转为布尔值
print(f"\nbool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f"bool('hello') = {bool('hello')}")
print(f"bool('') = {bool('')}")
print(f"bool([1, 2, 3]) = {bool([1, 2, 3])}")
print(f"bool([]) = {bool([])}")

# 【变量赋值和交换】
print("\n【6. 变量赋值和交换】")
x = 5
y = 10
print(f"交换前: x = {x}, y = {y}")
x, y = y, x  # Python 特有的优雅交换方式
print(f"交换后: x = {x}, y = {y}")

# 多重赋值
print("\n【多重赋值】")
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

print("\n✅ 所有数据类型知识点学习完成！\n")
