#!/usr/bin/env python3
"""
案例 09: 模块和导入
知识点：
  - 导入模块
  - 导入特定函数或类
  - 别名导入
  - 模块的 __name__ 和 __main__
  - 标准库常用模块
"""

import sys
import os
from datetime import datetime, timedelta
from math import pi, sqrt
import json
import random

print("=" * 60)
print("案例 09: 模块和导入")
print("=" * 60)

# 【导入模块的不同方式】
print("\n【1. 导入模块的不同方式】")

# 方式1: 导入整个模块
print("方式1: import sys")
print(f"  sys.version = {sys.version[:30]}...")
print(f"  sys.platform = {sys.platform}")

# 方式2: 导入特定的对象
print("\\n方式2: from math import pi, sqrt")
print(f"  pi = {pi}")
print(f"  sqrt(16) = {sqrt(16)}")

# 方式3: 导入所有对象 (不推荐)
print("\\n方式3: from datetime import * (不推荐)")
from datetime import *

# 方式4: 别名导入
print("\\n方式4: 别名导入")
import datetime as dt
now = dt.datetime.now()
print(f"  当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 【常用标准库】
print("\n【2. 常用标准库】")

# datetime - 日期和时间
print("\\ndatetime - 日期和时间:")
now = datetime.now()
print(f"  现在: {now}")
print(f"  年月日: {now.year}-{now.month:02d}-{now.day:02d}")
tomorrow = now + timedelta(days=1)
print(f"  明天: {tomorrow.date()}")

# random - 随机数
print("\\nrandom - 随机数:")
print(f"  random.random() = {random.random()}")
print(f"  random.randint(1, 100) = {random.randint(1, 100)}")
print(f"  random.choice([1,2,3,4,5]) = {random.choice([1, 2, 3, 4, 5])}")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"  random.shuffle([1,2,3,4,5]) = {numbers}")

# os - 操作系统
print("\\nos - 操作系统:")
print(f"  os.getcwd() = {os.getcwd()}")
print(f"  os.name = {os.name}")
print(f"  os.sep = '{os.sep}'")

# json - JSON 处理
print("\\njson - JSON 处理:")
data = {"name": "张三", "age": 25, "hobbies": ["读书", "游泳"]}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(f"  json.dumps():")
print(json_str)

# 【模块搜索路径】
print("\n【3. 模块搜索路径】")
print(f"sys.path:")
for path in sys.path[:3]:  # 只显示前 3 个
    print(f"  {path}")

# 【检查模块】
print("\n【4. 检查模块中的内容】")
print(f"dir(math)[:10] = {dir(__import__('math'))[:10]}")
print(f"\\nhasattr(math, 'pi') = {hasattr(__import__('math'), 'pi')}")
print(f"getattr(math, 'pi') = {getattr(__import__('math'), 'pi')}")

# 【创建和导入自定义模块】
print("\n【5. 创建自定义模块】")

# 创建一个简单的模块
module_path = "d:\\work\\projects\\figer\\python-service\\examples"
my_module_file = os.path.join(module_path, "my_math_module.py")

module_code = '''"""
自定义数学模块
"""

def add(a, b):
    """两数相加"""
    return a + b

def subtract(a, b):
    """两数相减"""
    return a - b

def multiply(a, b):
    """两数相乘"""
    return a * b

def divide(a, b):
    """两数相除"""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b

PI = 3.14159
'''

if not os.path.exists(my_module_file):
    with open(my_module_file, "w", encoding="utf-8") as f:
        f.write(module_code)
    print(f"  自定义模块已创建: {my_module_file}")
else:
    print(f"  自定义模块已存在: {my_module_file}")

# 动态导入模块
sys.path.insert(0, module_path)
import my_math_module

print("\\n使用自定义模块:")
print(f"  my_math_module.add(5, 3) = {my_math_module.add(5, 3)}")
print(f"  my_math_module.multiply(4, 5) = {my_math_module.multiply(4, 5)}")
print(f"  my_math_module.PI = {my_math_module.PI}")

# 【__name__ 和 __main__】
print("\n【6. __name__ 和 __main__】")

print(f"当前脚本的 __name__ = '{__name__}'")

# 创建一个有 if __name__ == '__main__' 的模块
test_module_file = os.path.join(module_path, "test_main_module.py")
test_module_code = '''"""
演示 __name__ 和 __main__ 的模块
"""

def hello():
    print("  Hello from module!")

if __name__ == "__main__":
    print("这个模块被直接运行了")
    hello()
else:
    print("这个模块被导入了")
    hello()
'''

if not os.path.exists(test_module_file):
    with open(test_module_file, "w", encoding="utf-8") as f:
        f.write(test_module_code)
    print(f"  测试模块已创建: {test_module_file}")

# 【模块和包】
print("\n【7. 包 (Package)】")

# 创建一个包
package_path = os.path.join(module_path, "my_package")
if not os.path.exists(package_path):
    os.makedirs(package_path)
    
    # 创建 __init__.py
    with open(os.path.join(package_path, "__init__.py"), "w", encoding="utf-8") as f:
        f.write('"""我的包"""\n\nversion = "1.0.0"')
    
    # 创建子模块
    with open(os.path.join(package_path, "utils.py"), "w", encoding="utf-8") as f:
        f.write('def greet(name):\n    return f"Hello, {name}!"')
    
    print(f"  包已创建: {package_path}")

# 导入包中的模块
import my_package.utils
print(f"  my_package.utils.greet('Alice') = {my_package.utils.greet('Alice')}")

# 【模块的重新加载】
print("\n【8. 模块信息】")
print(f"sys.modules 中的模块数: {len(sys.modules)}")
print(f"\\n已导入的模块 (部分):")
for i, mod_name in enumerate(list(sys.modules.keys())[:5]):
    print(f"  {i+1}. {mod_name}")

# 【实用案例】
print("\n【9. 实用案例】")

# 案例: 构建一个简单的计算器模块
print("\\n案例: 简单计算器")

calc_file = os.path.join(module_path, "simple_calc.py")
calc_code = '''"""
简单计算器模块
"""

class Calculator:
    def __init__(self):
        self.history = []
    
    def calculate(self, expr):
        """计算表达式"""
        try:
            result = eval(expr)
            self.history.append(f"{expr} = {result}")
            return result
        except Exception as e:
            return f"错误: {e}"
    
    def show_history(self):
        """显示计算历史"""
        return self.history

if __name__ == "__main__":
    calc = Calculator()
    print("简单计算器")
    while True:
        expr = input("输入表达式 (quit 退出): ").strip()
        if expr.lower() == "quit":
            break
        result = calc.calculate(expr)
        print(f"结果: {result}")
    print("\\n计算历史:")
    for item in calc.show_history():
        print(f"  {item}")
'''

if not os.path.exists(calc_file):
    with open(calc_file, "w", encoding="utf-8") as f:
        f.write(calc_code)
    print(f"  计算器模块已创建")

import simple_calc
calc = simple_calc.Calculator()
print(f"  1+2+3 = {calc.calculate('1+2+3')}")
print(f"  10*5 = {calc.calculate('10*5')}")
print(f"  计算历史: {calc.show_history()}")

print("\n✅ 模块和导入学习完成！\n")
