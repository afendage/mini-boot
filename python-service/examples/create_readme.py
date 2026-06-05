#!/usr/bin/env python3
"""
Python 学习案例导览 - README
"""

# 创建 README 文件的内容
readme_content = """
# Python 完全学习指南 - 15 个案例

欢迎使用 Python 学习案例集！这是一份适合 Python 初学者的完整学习资源。

## 📚 学习路线

### 第一阶段：基础语法 (案例 0-5)
- **案例 00: Hello Python** ⭐ 从这里开始！
  - 学习基础输出、变量、注释
  
- **案例 01: 变量和数据类型**
  - int, float, str, bool 类型
  - 类型转换、类型检查
  
- **案例 02: 字符串操作和格式化**
  - 字符串索引、切片、方法
  - f-string、format() 等格式化方式
  
- **案例 03: 列表和元组**
  - 列表的创建、修改、方法
  - 元组和列表的区别
  
- **案例 04: 字典和集合**
  - 字典的键值对操作
  - 集合的数学运算
  
- **案例 05: 控制流**
  - if/elif/else 条件语句
  - for 和 while 循环
  - break, continue, pass

### 第二阶段：函数和组织 (案例 6-9)
- **案例 06: 函数**
  - 函数定义和调用
  - 参数、返回值、lambda
  
- **案例 07: 文件 I/O 和异常处理**
  - 读写文件、with 语句
  - try/except/finally 异常处理
  
- **案例 08: 面向对象编程**
  - 类、对象、属性、方法
  - 继承、多态、特殊方法
  
- **案例 09: 模块和导入**
  - 导入模块、标准库
  - 创建自定义模块

### 第三阶段：高级特性 (案例 10-13)
- **案例 10: 列表推导式和推导式**
  - 列表推导式、字典推导式、集合推导式
  - 生成器表达式
  
- **案例 11: 装饰器**
  - 装饰器基础、带参数的装饰器
  - functools.wraps、实际应用
  
- **案例 12: 生成器**
  - yield 关键字、延迟计算
  - 内存效率、链式操作
  
- **案例 13: JSON 处理**
  - json.dumps()、json.loads()
  - 文件读写、自定义对象序列化

### 第四阶段：进阶主题 (案例 14-15)
- **案例 14: 数据结构和算法**
  - 栈、队列、链表
  - 排序和搜索算法
  - 图的基本操作
  
- **案例 15: 综合项目 - 学生管理系统**
  - 集成所有学习内容
  - 真实项目示例

## 🚀 快速开始

### 方式一：运行主菜单程序
```bash
cd python-service/examples
python main.py
```
然后选择要学习的案例编号（1-16）

### 方式二：直接运行单个案例
```bash
# 运行某个特定案例
python 00_hello.py
python 01_variables_and_types.py
python 15_comprehensive_project.py
```

### 方式三：在 VS Code 中运行
1. 打开 examples 目录中的任何 .py 文件
2. 点击右上角的"运行"按钮
3. 查看输出结果

## 📖 学习建议

### ⏱️ 学习时间安排
- 基础阶段（案例 0-5）：3-5 天
- 函数阶段（案例 6-9）：3-5 天
- 高级阶段（案例 10-13）：3-5 天
- 进阶阶段（案例 14-15）：2-3 天
- **总计：2-3 周即可掌握 Python 核心知识**

### 📝 学习方法
1. **逐个运行案例**：按顺序运行每个案例，观察输出
2. **理解代码**：阅读代码注释，理解每个知识点
3. **修改实验**：修改代码参数，观察不同的运行结果
4. **动手练习**：根据案例创意，编写自己的代码
5. **查看输出**：每个案例都有清晰的输出，看到实际效果

### 💡 核心知识点速记

**变量和类型**
```python
name = "张三"  # 字符串
age = 25  # 整数
height = 1.75  # 浮点数
is_student = True  # 布尔值
```

**集合类型**
```python
my_list = [1, 2, 3]  # 列表 (可变)
my_tuple = (1, 2, 3)  # 元组 (不可变)
my_dict = {"name": "张三"}  # 字典
my_set = {1, 2, 3}  # 集合
```

**控制流**
```python
if condition:
    # 代码
elif other_condition:
    # 代码
else:
    # 代码

for item in items:
    # 循环
    
while condition:
    # 循环
```

**函数**
```python
def greet(name, greeting="你好"):
    \"\"\"函数文档\"\"\"
    return f"{greeting}, {name}!"

# 调用
greet("Alice")
```

**类**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"你好，我是 {self.name}"

# 使用
person = Person("张三", 25)
```

**异常处理**
```python
try:
    # 可能出错的代码
    result = 10 / 0
except ZeroDivisionError:
    # 处理异常
    print("不能除以 0")
except Exception as e:
    # 处理其他异常
    print(f"发生异常: {e}")
finally:
    # 无论是否出错都执行
    print("清理工作")
```

**列表推导式**
```python
# 创建新列表
squares = [x**2 for x in range(10)]

# 条件过滤
even = [x for x in range(10) if x % 2 == 0]

# 字典推导式
dict_comp = {x: x**2 for x in range(5)}
```

**生成器**
```python
def count_up(n):
    for i in range(n):
        yield i  # 产生值

# 使用
for num in count_up(5):
    print(num)
```

## 📂 文件结构

```
python-service/
├── examples/
│   ├── main.py                      # 主菜单程序
│   ├── 00_hello.py                  # 案例 0
│   ├── 01_variables_and_types.py    # 案例 1
│   ├── ...
│   ├── 15_comprehensive_project.py  # 案例 15
│   ├── my_math_module.py            # 自定义模块 (案例 9 生成)
│   ├── my_package/                  # 自定义包 (案例 9 生成)
│   └── sample_files/                # 示例文件存储
│       ├── sample.txt
│       ├── config.json
│       └── students_data.json
├── app.py                           # Flask 应用
├── requirements.txt
└── README.md
```

## 🎯 学习目标

完成所有 15 个案例后，你将掌握：

✅ Python 基础语法和数据类型
✅ 流程控制和函数
✅ 文件操作和异常处理
✅ 面向对象编程
✅ 模块和包的使用
✅ 高级特性（推导式、装饰器、生成器）
✅ JSON 数据处理
✅ 数据结构和算法
✅ 实际项目开发能力

## 🔗 相关资源

- [Python 官方文档](https://docs.python.org/3/)
- [Python 风格指南 (PEP 8)](https://www.python.org/dev/peps/pep-0008/)
- [Real Python](https://realpython.com/)
- [W3Schools Python 教程](https://www.w3schools.com/python/)

## ❓ 常见问题

**Q: 我应该按照什么顺序学习？**
A: 强烈建议按照案例 0-15 的顺序学习。每个案例都建立在前面知识的基础上。

**Q: 如果我不理解某个概念怎么办？**
A: 多运行几次代码，修改参数观察结果。也可以查看官方文档或网络资源获得更多解释。

**Q: 我可以修改代码吗？**
A: 完全可以！实际上强烈建议修改代码进行实验。这是最好的学习方式。

**Q: 需要记住所有的代码吗？**
A: 不需要。理解概念比记住代码更重要。多练习，自然会记住常用的代码模式。

**Q: 学完这些就可以工作了吗？**
A: 这些案例涵盖了 Python 的核心知识。之后你可以学习特定领域的库（Web 框架、数据科学等）来解决实际问题。

## 📧 反馈建议

如果你对这些学习案例有任何建议或发现问题，欢迎提出改进意见！

## 📄 许可证

这些学习案例可自由使用和修改。

---

**祝你学习愉快！Happy Learning! 🎉**

开始从案例 00 学习吧：`python 00_hello.py`
"""

if __name__ == "__main__":
    # 创建 README
    readme_path = "d:\\work\\projects\\figer\\python-service\\examples\\README_LEARNING_GUIDE.md"
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"✅ README 文件已创建: {readme_path}")
