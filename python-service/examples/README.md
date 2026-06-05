# Python 完全学习指南 - 15 个实践案例

这是一套完整的 Python 学习资源，从基础到进阶，包含 15 个可运行的学习案例。

## 🎯 快速开始

### 方式1: 使用菜单运行
```bash
cd python-service/examples
python main.py
```

### 方式2: 直接运行某个案例
```bash
python 00_hello.py              # Hello Python
python 01_variables_and_types.py   # 变量和类型
python 15_comprehensive_project.py # 综合项目
```

## 📚 15 个学习案例

| # | 文件 | 主题 | 难度 | 学习要点 |
|---|------|------|------|---------|
| 0 | 00_hello.py | Hello Python | ⭐ | 基础输出、变量、注释 |
| 1 | 01_variables_and_types.py | 变量和类型 | ⭐ | int, float, str, bool, 类型转换 |
| 2 | 02_strings.py | 字符串操作 | ⭐ | 索引、切片、方法、格式化 |
| 3 | 03_lists_and_tuples.py | 列表和元组 | ⭐⭐ | 创建、修改、遍历、方法 |
| 4 | 04_dictionaries_and_sets.py | 字典和集合 | ⭐⭐ | 键值对、集合运算 |
| 5 | 05_control_flow.py | 控制流 | ⭐⭐ | if/for/while 循环、break/continue |
| 6 | 06_functions.py | 函数 | ⭐⭐ | 定义、参数、返回值、lambda |
| 7 | 07_file_io.py | 文件和异常 | ⭐⭐⭐ | 读写文件、try/except、自定义异常 |
| 8 | 08_oop_classes.py | 面向对象编程 | ⭐⭐⭐ | 类、继承、多态、特殊方法 |
| 9 | 09_modules_and_imports.py | 模块和导入 | ⭐⭐⭐ | 导入、标准库、自定义模块 |
| 10 | 10_list_comprehension.py | 推导式 | ⭐⭐⭐ | 列表推导式、字典推导式、生成器表达式 |
| 11 | 11_decorators.py | 装饰器 | ⭐⭐⭐⭐ | 装饰器、functools.wraps、实际应用 |
| 12 | 12_generators.py | 生成器 | ⭐⭐⭐⭐ | yield、延迟计算、内存效率 |
| 13 | 13_json_handling.py | JSON 处理 | ⭐⭐ | dumps/loads、文件操作、序列化 |
| 14 | 14_data_structures.py | 数据结构和算法 | ⭐⭐⭐⭐ | 栈、队列、排序、搜索、图 |
| 15 | 15_comprehensive_project.py | 综合项目 | ⭐⭐⭐⭐ | 学生管理系统、完整应用 |

## 📖 学习路线建议

### 第一周：基础语法
- 案例 0-5：掌握基本数据类型和控制流
- 预计时间：3-5 天
- 目标：能够编写简单的 Python 脚本

### 第二周：函数和组织
- 案例 6-9：学习函数、文件操作、OOP、模块
- 预计时间：3-5 天  
- 目标：能够组织代码和编写简单的类

### 第三周：高级特性
- 案例 10-13：掌握推导式、装饰器、生成器、JSON
- 预计时间：3-5 天
- 目标：理解 Python 的高级特性

### 第四周：进阶主题
- 案例 14-15：数据结构、算法、实际项目
- 预计时间：2-3 天
- 目标：能够完成实际项目开发

## 💡 学习技巧

1. **逐行运行** - 不要跳过，每个案例都有清晰的输出
2. **修改实验** - 更改参数和代码，观察结果变化
3. **写笔记** - 记录关键概念和语法
4. **动手练习** - 完成每个案例后，自己编写类似的代码
5. **查看源码** - 阅读代码注释和文档字符串

## 📁 文件结构

```
examples/
├── main.py                          # 菜单程序
├── 00_hello.py 到 15_comprehensive_project.py
├── my_math_module.py                # (自动生成) 自定义模块
├── my_package/                      # (自动生成) 自定义包
├── simple_calc.py                   # (自动生成) 计算器模块
├── test_main_module.py              # (自动生成) 测试模块
└── sample_files/                    # (自动生成) 示例数据文件
    ├── sample.txt
    ├── config.json
    ├── students.json
    └── students_data.json
```

## ✨ 核心知识点

### 基础数据类型
```python
# 字符串
name = "Python"
print(f"Hello, {name}!")

# 列表
items = [1, 2, 3, 4, 5]
items.append(6)

# 字典
person = {"name": "Alice", "age": 30}
print(person["name"])

# 集合
unique = {1, 2, 2, 3, 3, 3}
print(unique)  # {1, 2, 3}
```

### 控制流
```python
# if 语句
if age >= 18:
    print("成年人")
else:
    print("未成年人")

# for 循环
for i in range(5):
    print(i)

# while 循环
while condition:
    # 代码
    break
```

### 函数
```python
def greet(name, greeting="你好"):
    """问候函数"""
    return f"{greeting}, {name}!"

# 调用
result = greet("Alice")
```

### 类
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"我是 {self.name}，{self.age} 岁"

person = Person("张三", 25)
print(person.introduce())
```

### 异常处理
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"错误: {e}")
except Exception as e:
    print(f"未知错误: {e}")
finally:
    print("清理完成")
```

### 列表推导式
```python
# 创建平方列表
squares = [x**2 for x in range(10)]

# 条件过滤
evens = [x for x in range(10) if x % 2 == 0]

# 字典推导式
dict_comp = {x: x**2 for x in range(5)}
```

## 🎓 完成后你能做什么

- ✅ 编写 Python 脚本和程序
- ✅ 使用 Python 的标准库
- ✅ 编写面向对象的 Python 代码
- ✅ 处理文件和异常
- ✅ 使用高级特性（推导式、装饰器等）
- ✅ 开发完整的应用程序
- ✅ 学习 Web 框架（Flask、Django）
- ✅ 进入数据科学领域（Pandas、NumPy）
- ✅ 参与 Python 项目开发

## 📚 推荐资源

- [Python 官方文档](https://docs.python.org/3/)
- [Real Python 教程](https://realpython.com/)
- [LeetCode Python 题库](https://leetcode.com/)
- [GeeksforGeeks Python](https://www.geeksforgeeks.org/python-programming-language/)

## 🚀 下一步学习

完成这 15 个案例后，你可以：

1. **Web 开发** - 学习 Flask 或 Django
2. **数据科学** - 学习 Pandas, NumPy, Matplotlib
3. **自动化脚本** - 使用 Python 自动化日常任务
4. **机器学习** - 学习 Scikit-learn, TensorFlow
5. **游戏开发** - 学习 Pygame

## 💬 提示

- 不要跳过任何案例
- 多次运行代码，修改参数
- 理解概念比记住语法更重要
- 坚持每天学习，2-3 周即可掌握核心知识
- 遇到问题时，查看代码注释和官方文档

---

**准备好了吗？现在就开始吧！**

```bash
python main.py
```

或者直接运行第一个案例：
```bash
python 00_hello.py
```

祝你学习愉快！🎉
