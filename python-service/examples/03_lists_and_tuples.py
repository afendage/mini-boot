#!/usr/bin/env python3
"""
案例 03: 列表和元组
知识点：
  - 列表的创建、索引、切片
  - 列表的方法 (append, extend, insert, remove, pop, sort, reverse)
  - 元组 (不可变序列)
  - 序列的通用操作
"""

print("=" * 60)
print("案例 03: 列表和元组")
print("=" * 60)

# 【列表的创建】
print("\n【1. 列表的创建】")
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True, None]
nested = [[1, 2], [3, 4], [5, 6]]

print(f"empty_list = {empty_list}")
print(f"numbers = {numbers}")
print(f"mixed = {mixed}")
print(f"nested = {nested}")

# 使用 list() 函数
print(f"list(range(5)) = {list(range(5))}")
print(f"list('ABC') = {list('ABC')}")

# 【列表的索引和切片】
print("\n【2. 列表的索引和切片】")
nums = [10, 20, 30, 40, 50]
print(f"nums = {nums}")
print(f"nums[0] = {nums[0]}")  # 第一个元素
print(f"nums[-1] = {nums[-1]}")  # 最后一个元素
print(f"nums[1:4] = {nums[1:4]}")  # 切片
print(f"nums[:3] = {nums[:3]}")  # 前三个
print(f"nums[2:] = {nums[2:]}")  # 从第 3 个开始
print(f"nums[::2] = {nums[::2]}")  # 每隔 2 个取一个
print(f"nums[::-1] = {nums[::-1]}")  # 反向

# 【列表的修改】
print("\n【3. 列表的修改】")
nums = [1, 2, 3, 4, 5]
print(f"原列表: {nums}")
nums[0] = 10
print(f"修改 nums[0] = 10: {nums}")
nums[1:3] = [20, 30, 40]  # 切片替换
print(f"修改 nums[1:3] = [20, 30, 40]: {nums}")

# 【列表的方法】
print("\n【4. 列表的方法】")

# append() - 添加单个元素
print("\nappend() - 添加单个元素:")
fruits = ["apple", "banana"]
print(f"原列表: {fruits}")
fruits.append("orange")
print(f"append('orange'): {fruits}")

# extend() - 添加多个元素
print("\nextend() - 添加多个元素:")
fruits = ["apple", "banana"]
fruits.extend(["cherry", "date"])
print(f"extend(['cherry', 'date']): {fruits}")

# insert() - 在指定位置插入
print("\ninsert() - 在指定位置插入:")
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print(f"insert(1, 'orange'): {fruits}")

# remove() - 删除指定值
print("\nremove() - 删除指定值:")
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(f"remove('banana'): {fruits}")

# pop() - 删除并返回指定位置的元素
print("\npop() - 删除并返回指定位置的元素:")
fruits = ["apple", "banana", "cherry"]
popped = fruits.pop(1)
print(f"pop(1) 返回: {popped}")
print(f"列表变为: {fruits}")
last = fruits.pop()  # 删除最后一个
print(f"pop() 返回: {last}")
print(f"列表变为: {fruits}")

# index() - 获取元素的索引
print("\nindex() - 获取元素的索引:")
fruits = ["apple", "banana", "cherry", "banana"]
print(f"列表: {fruits}")
print(f"index('banana') = {fruits.index('banana')}")

# count() - 计数
print("\ncount() - 计数:")
numbers = [1, 2, 2, 3, 2, 4, 5]
print(f"列表: {numbers}")
print(f"count(2) = {numbers.count(2)}")

# sort() - 排序
print("\nsort() - 排序:")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"原列表: {numbers}")
numbers.sort()
print(f"sort() 后: {numbers}")
numbers.sort(reverse=True)
print(f"sort(reverse=True): {numbers}")

# reverse() - 反向
print("\nreverse() - 反向:")
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(f"reverse() 后: {numbers}")

# clear() - 清空列表
print("\nclear() - 清空列表:")
numbers = [1, 2, 3]
print(f"原列表: {numbers}")
numbers.clear()
print(f"clear() 后: {numbers}")

# copy() - 复制列表
print("\ncopy() - 复制列表:")
original = [1, 2, 3]
copy_list = original.copy()
copy_list.append(4)
print(f"original: {original}")
print(f"copy_list: {copy_list}")

# 【列表的通用操作】
print("\n【5. 列表的通用操作】")
nums = [1, 2, 3, 4, 5]
print(f"列表: {nums}")
print(f"len(nums) = {len(nums)}")  # 长度
print(f"min(nums) = {min(nums)}")  # 最小值
print(f"max(nums) = {max(nums)}")  # 最大值
print(f"sum(nums) = {sum(nums)}")  # 求和
print(f"2 in nums = {2 in nums}")  # 判断是否存在
print(f"10 in nums = {10 in nums}")

# 【元组】
print("\n【6. 元组 (Tuple)】")
print("元组是不可变的序列")

# 创建元组
empty_tuple = ()
single_tuple = (1,)  # 单元素元组需要逗号
tuple1 = (1, 2, 3, 4, 5)
mixed_tuple = (1, "hello", 3.14, True)
nested_tuple = ((1, 2), (3, 4), (5, 6))

print(f"empty_tuple = {empty_tuple}")
print(f"single_tuple = {single_tuple}")
print(f"tuple1 = {tuple1}")
print(f"mixed_tuple = {mixed_tuple}")

# 元组的操作
print(f"\ntuple1[0] = {tuple1[0]}")
print(f"tuple1[1:3] = {tuple1[1:3]}")
print(f"len(tuple1) = {len(tuple1)}")
print(f"1 in tuple1 = {1 in tuple1}")

# 元组解包
print("\n元组解包:")
x, y, z = (1, 2, 3)
print(f"x, y, z = (1, 2, 3)")
print(f"x = {x}, y = {y}, z = {z}")

# 列表和元组的转换
print("\n列表和元组的转换:")
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
back_to_list = list(my_tuple)
print(f"list: {my_list}")
print(f"tuple: {my_tuple}")
print(f"back to list: {back_to_list}")

# 【实用案例】
print("\n【7. 实用案例】")
# 购物车计算总价
print("\n购物车计算:")
items = [("苹果", 10, 2), ("香蕉", 8, 3), ("橙子", 12, 1)]
total = 0
print("商品\t单价\t数量\t小计")
print("-" * 30)
for name, price, quantity in items:
    subtotal = price * quantity
    total += subtotal
    print(f"{name}\t{price}\t{quantity}\t{subtotal}")
print("-" * 30)
print(f"总计: {total}")

print("\n✅ 列表和元组学习完成！\n")
