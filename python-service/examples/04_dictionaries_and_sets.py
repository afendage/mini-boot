#!/usr/bin/env python3
"""
案例 04: 字典和集合
知识点：
  - 字典的创建、访问、修改
  - 字典的方法
  - 集合的创建、操作
  - 集合的数学运算
"""

print("=" * 60)
print("案例 04: 字典和集合")
print("=" * 60)

# 【字典的创建】
print("\n【1. 字典的创建】")
empty_dict = {}
person = {"name": "张三", "age": 25, "city": "北京"}
student = dict(name="李四", age=22, major="计算机")

print(f"empty_dict = {empty_dict}")
print(f"person = {person}")
print(f"student = {student}")

# 【字典的访问】
print("\n【2. 字典的访问】")
person = {"name": "张三", "age": 25, "city": "北京"}
print(f"person['name'] = {person['name']}")
print(f"person['age'] = {person['age']}")
print(f"person.get('city') = {person.get('city')}")
print(f"person.get('phone', '未知') = {person.get('phone', '未知')}")  # 使用默认值

# 【字典的修改】
print("\n【3. 字典的修改】")
person = {"name": "张三", "age": 25}
print(f"原字典: {person}")

# 更新值
person["age"] = 26
print(f"修改 age: {person}")

# 添加新键值对
person["city"] = "北京"
print(f"添加 city: {person}")

# update() - 批量更新
person.update({"phone": "123456", "email": "zhangsan@example.com"})
print(f"update() 后: {person}")

# 【字典的方法】
print("\n【4. 字典的方法】")

person = {"name": "张三", "age": 25, "city": "北京"}

# keys() - 获取所有键
print(f"person.keys() = {list(person.keys())}")

# values() - 获取所有值
print(f"person.values() = {list(person.values())}")

# items() - 获取所有键值对
print(f"person.items() = {list(person.items())}")

# pop() - 删除并返回值
age = person.pop("age")
print(f"pop('age') = {age}")
print(f"person = {person}")

# popitem() - 删除最后一个键值对
print(f"\nperson = {person}")
key, value = person.popitem()
print(f"popitem() 返回: ({key}, {value})")
print(f"person = {person}")

# clear() - 清空字典
test_dict = {"a": 1, "b": 2}
test_dict.clear()
print(f"clear() 后: {test_dict}")

# 【字典的遍历】
print("\n【5. 字典的遍历】")
person = {"name": "张三", "age": 25, "city": "北京"}

print("遍历键:")
for key in person:
    print(f"  {key}: {person[key]}")

print("\n遍历键值对:")
for key, value in person.items():
    print(f"  {key}: {value}")

print("\n遍历值:")
for value in person.values():
    print(f"  {value}")

# 【嵌套字典】
print("\n【6. 嵌套字典】")
company = {
    "employees": [
        {"name": "张三", "position": "经理", "salary": 10000},
        {"name": "李四", "position": "工程师", "salary": 8000},
        {"name": "王五", "position": "设计师", "salary": 7000}
    ],
    "location": "北京",
    "founded": 2020
}

print(f"公司位置: {company['location']}")
print(f"第一个员工: {company['employees'][0]['name']}")
print(f"第二个员工的职位: {company['employees'][1]['position']}")

print("\n所有员工:")
for emp in company["employees"]:
    print(f"  {emp['name']} - {emp['position']} - {emp['salary']}元")

# 【集合 (Set)】
print("\n【7. 集合 (Set)】")
print("集合是无序的、不重复的、可变的")

# 创建集合
empty_set = set()
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}
from_string = set("hello")  # 将字符串转为集合

print(f"empty_set = {empty_set}")
print(f"numbers = {numbers}")
print(f"mixed_set = {mixed_set}")
print(f"set('hello') = {from_string}")

# 集合会自动去重
duplicates = {1, 1, 2, 2, 3, 3}
print(f"{{1, 1, 2, 2, 3, 3}} = {duplicates}")

# 【集合的方法】
print("\n【8. 集合的方法】")

# add() - 添加元素
print("\nadd() - 添加元素:")
s = {1, 2, 3}
s.add(4)
print(f"add(4): {s}")

# remove() - 删除元素 (不存在会报错)
print("\nremove() - 删除元素:")
s = {1, 2, 3}
s.remove(2)
print(f"remove(2): {s}")

# discard() - 删除元素 (不存在不报错)
print("\ndiscard() - 删除元素:")
s = {1, 2, 3}
s.discard(4)  # 不存在也不报错
print(f"discard(4): {s}")

# pop() - 删除并返回一个元素
print("\npop() - 删除并返回一个元素:")
s = {1, 2, 3}
elem = s.pop()
print(f"pop() 返回: {elem}, 集合: {s}")

# clear() - 清空集合
print("\nclear() - 清空集合:")
s = {1, 2, 3}
s.clear()
print(f"clear() 后: {s}")

# 【集合的数学运算】
print("\n【9. 集合的数学运算】")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"set_a = {set_a}")
print(f"set_b = {set_b}")
print()

# 并集 (Union)
print(f"set_a | set_b (并集) = {set_a | set_b}")
print(f"set_a.union(set_b) = {set_a.union(set_b)}")

# 交集 (Intersection)
print(f"set_a & set_b (交集) = {set_a & set_b}")
print(f"set_a.intersection(set_b) = {set_a.intersection(set_b)}")

# 差集 (Difference)
print(f"set_a - set_b (差集) = {set_a - set_b}")
print(f"set_a.difference(set_b) = {set_a.difference(set_b)}")

# 对称差 (Symmetric Difference)
print(f"set_a ^ set_b (对称差) = {set_a ^ set_b}")
print(f"set_a.symmetric_difference(set_b) = {set_a.symmetric_difference(set_b)}")

# 【实用案例】
print("\n【10. 实用案例】")

# 案例1: 找出重复元素
print("\n案例1: 找出重复元素")
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(numbers)
print(f"原列表: {numbers}")
print(f"去重后: {sorted(list(unique))}")

# 案例2: 比较两个列表的差异
print("\n案例2: 比较两个列表的差异")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
set1 = set(list1)
set2 = set(list2)
print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"只在 list1 中: {set1 - set2}")
print(f"只在 list2 中: {set2 - set1}")
print(f"两个都有: {set1 & set2}")
print(f"至少在一个中: {set1 | set2}")

# 案例3: 学生选课分析
print("\n案例3: 学生选课分析")
python_students = {"张三", "李四", "王五", "赵六"}
java_students = {"张三", "王五", "孙七", "周八"}

print(f"选 Python 的学生: {python_students}")
print(f"选 Java 的学生: {java_students}")
print(f"两个都选的学生: {python_students & java_students}")
print(f"只选 Python 的学生: {python_students - java_students}")
print(f"只选 Java 的学生: {java_students - python_students}")
print(f"至少选一个的学生: {python_students | java_students}")

print("\n✅ 字典和集合学习完成！\n")
