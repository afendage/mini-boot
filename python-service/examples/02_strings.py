#!/usr/bin/env python3
"""
案例 02: 字符串操作和格式化
知识点：
  - 字符串索引和切片
  - 字符串方法
  - 字符串格式化（f-string, format(), %)
  - 字符串转义
"""

print("=" * 60)
print("案例 02: 字符串操作和格式化")
print("=" * 60)

# 【字符串索引】
print("\n【1. 字符串索引】")
text = "Python"
print(f"text = '{text}'")
print(f"text[0] = '{text[0]}'  # 第一个字符")
print(f"text[1] = '{text[1]}'  # 第二个字符")
print(f"text[-1] = '{text[-1]}'  # 最后一个字符")
print(f"text[-2] = '{text[-2]}'  # 倒数第二个字符")

# 【字符串切片】
print("\n【2. 字符串切片】")
text = "Hello Python"
print(f"text = '{text}'")
print(f"text[0:5] = '{text[0:5]}'  # 从 0 到 5 (不包括 5)")
print(f"text[6:] = '{text[6:]}'  # 从 6 到末尾")
print(f"text[:5] = '{text[:5]}'  # 从开始到 5")
print(f"text[::2] = '{text[::2]}'  # 每隔 2 个字符取一个")
print(f"text[::-1] = '{text[::-1]}'  # 反向字符串")

# 【字符串方法】
print("\n【3. 字符串方法】")
text = "Hello World"

print("\n大小写转换:")
print(f"text.upper() = '{text.upper()}'")
print(f"text.lower() = '{text.lower()}'")
print(f"text.capitalize() = '{text.capitalize()}'")
print(f"text.swapcase() = '{text.swapcase()}'")

print("\n查找和替换:")
print(f"text.find('World') = {text.find('World')}")
print(f"text.find('xyz') = {text.find('xyz')}")  # 不存在返回 -1
print(f"text.count('l') = {text.count('l')}")
print(f"text.replace('World', 'Python') = '{text.replace('World', 'Python')}'")

print("\n分割和连接:")
words = "apple,banana,orange"
print(f"'{words}'.split(',') = {words.split(',')}")
fruit_list = ["apple", "banana", "orange"]
print(f"', '.join(['apple', 'banana', 'orange']) = '{', '.join(fruit_list)}'")

print("\n判断:")
print(f"'hello'.startswith('he') = {'hello'.startswith('he')}")
print(f"'hello'.endswith('lo') = {'hello'.endswith('lo')}")
print(f"'hello123'.isdigit() = {'hello123'.isdigit()}")
print(f"'12345'.isdigit() = {'12345'.isdigit()}")
print(f"'hello'.isalpha() = {'hello'.isalpha()}")
print(f"'hello123'.isalnum() = {'hello123'.isalnum()}")

print("\n去除空格:")
text_with_space = "  hello world  "
print(f"'{text_with_space}' 长度: {len(text_with_space)}")
print(f"text.strip() = '{text_with_space.strip()}'")
print(f"text.lstrip() = '{text_with_space.lstrip()}'")
print(f"text.rstrip() = '{text_with_space.rstrip()}'")

# 【字符串格式化】
print("\n【4. 字符串格式化】")

# f-string (推荐，最现代的方式)
print("\nf-string 格式化 (Python 3.6+):")
name = "Alice"
age = 25
height = 1.75
print(f"我叫 {name}, 今年 {age} 岁, 身高 {height}m")
print(f"计算: 5 + 3 = {5 + 3}")
print(f"保留两位小数: π ≈ {3.14159:.2f}")
print(f"百分比: {0.75:.1%}")

# format() 方法
print("\nformat() 方法:")
print("我叫 {}, 今年 {} 岁".format(name, age))
print("我叫 {0}, {0} 住在中国".format(name))
print("我叫 {name}, 今年 {age} 岁".format(name=name, age=age))

# % 格式化 (旧方式，了解即可)
print("\n% 格式化 (旧方式):")
print("我叫 %s, 今年 %d 岁" % (name, age))

# 【字符串转义】
print("\n【5. 字符串转义】")
print("单引号: 'It\\'s a nice day'")
print('双引号: "He said \\"Hello\\""')
print("换行符: 第一行\n第二行\n第三行")
print("制表符: 姓名\t年龄\t城市\n张三\t25\t北京\n李四\t30\t上海")
print("反斜杠: C:\\Users\\Name\\Desktop")

# 【原始字符串】
print("\n【6. 原始字符串 (Raw String)】")
path = r"C:\Users\Name\Desktop"  # 使用 r 前缀，反斜杠不转义
print(f"path = {path}")
regex = r"^\d{3}-\d{4}$"  # 正则表达式
print(f"regex = {regex}")

# 【实用案例】
print("\n【7. 实用案例】")
# 生成一个表格
print("\n学生成绩表:")
print("-" * 40)
print("姓名\t语文\t数学\t英文\t平均分")
print("-" * 40)
students = [("张三", 90, 85, 88), ("李四", 95, 92, 89), ("王五", 88, 90, 85)]
for name, chinese, math, english in students:
    avg = (chinese + math + english) / 3
    print(f"{name}\t{chinese}\t{math}\t{english}\t{avg:.2f}")
print("-" * 40)

print("\n✅ 字符串操作和格式化学习完成！\n")
