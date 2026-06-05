#!/usr/bin/env python3
"""
案例 14: 常用数据结构和算法
知识点：
  - 栈 (Stack)
  - 队列 (Queue)
  - 链表 (Linked List)
  - 排序算法
  - 搜索算法
"""

from collections import deque, defaultdict
import time

print("=" * 60)
print("案例 14: 常用数据结构和算法")
print("=" * 60)

# 【栈 (Stack)】
print("\n【1. 栈 (Stack)】")
print("栈是 LIFO (后进先出) 的数据结构")

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """入栈"""
        self.items.append(item)
    
    def pop(self):
        """出栈"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """查看栈顶元素"""
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """检查栈是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """获取栈的大小"""
        return len(self.items)

print("栈操作示例:")
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"  push(1, 2, 3)")
print(f"  peek() = {stack.peek()}")
print(f"  pop() = {stack.pop()}")
print(f"  pop() = {stack.pop()}")

# 应用: 检查括号是否匹配
def is_balanced(s):
    """检查括号是否匹配"""
    stack = Stack()
    pairs = {"(": ")", "[": "]", "{": "}"}
    for char in s:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False
    return stack.is_empty()

print("\\n括号匹配检查:")
test_cases = ["([])", "([)]", "({[]})"]
for case in test_cases:
    result = "✅" if is_balanced(case) else "❌"
    print(f"  {result} {case}")

# 【队列 (Queue)】
print("\n【2. 队列 (Queue)】")
print("队列是 FIFO (先进先出) 的数据结构")

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        """入队"""
        self.items.append(item)
    
    def dequeue(self):
        """出队"""
        if not self.is_empty():
            return self.items.popleft()
        return None
    
    def is_empty(self):
        """检查队列是否为空"""
        return len(self.items) == 0
    
    def size(self):
        """获取队列大小"""
        return len(self.items)

print("队列操作示例:")
queue = Queue()
queue.enqueue("任务1")
queue.enqueue("任务2")
queue.enqueue("任务3")
print(f"  enqueue(任务1, 任务2, 任务3)")
print(f"  dequeue() = {queue.dequeue()}")
print(f"  dequeue() = {queue.dequeue()}")
print(f"  队列大小: {queue.size()}")

# 【排序算法】
print("\n【3. 排序算法】")

# 冒泡排序
def bubble_sort(arr):
    """冒泡排序"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print("冒泡排序:")
nums = [64, 34, 25, 12, 22, 11, 90]
print(f"  原数组: {nums}")
print(f"  排序后: {bubble_sort(nums.copy())}")

# 快速排序
def quick_sort(arr):
    """快速排序"""
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print("\\n快速排序:")
nums = [64, 34, 25, 12, 22, 11, 90]
print(f"  原数组: {nums}")
print(f"  排序后: {quick_sort(nums)}")

# 合并排序
def merge_sort(arr):
    """合并排序"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("\\n合并排序:")
nums = [64, 34, 25, 12, 22, 11, 90]
print(f"  原数组: {nums}")
print(f"  排序后: {merge_sort(nums)}")

# Python 内置排序
print("\\nPython 内置排序 (推荐使用):")
nums = [64, 34, 25, 12, 22, 11, 90]
print(f"  原数组: {nums}")
print(f"  sorted(nums) = {sorted(nums)}")
print(f"  nums.sort() = {nums}")

# 【搜索算法】
print("\n【4. 搜索算法】")

# 线性搜索
def linear_search(arr, target):
    """线性搜索"""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

print("线性搜索:")
nums = [12, 34, 25, 64, 22, 11, 90]
target = 64
index = linear_search(nums, target)
result = f"找到 (索引: {index})" if index != -1 else "未找到"
print(f"  在 {nums} 中搜索 {target}: {result}")

# 二分搜索
def binary_search(arr, target):
    """二分搜索 (需要排序的数组)"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print("\\n二分搜索:")
nums = sorted([12, 34, 25, 64, 22, 11, 90])
target = 64
index = binary_search(nums, target)
result = f"找到 (索引: {index})" if index != -1 else "未找到"
print(f"  在 {nums} 中搜索 {target}: {result}")

# 【递归算法】
print("\n【5. 递归算法】")

# 阶乘
def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("阶乘:")
for i in range(1, 6):
    print(f"  {i}! = {factorial(i)}")

# 斐波那契 (递归 vs 迭代)
def fibonacci_recursive(n):
    """斐波那契 (递归)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    """斐波那契 (迭代)"""
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

print("\\n斐波那契:")
print("  递归方式:")
for i in range(8):
    print(f"    fib({i}) = {fibonacci_recursive(i)}")

# 【动态规划】
print("\n【6. 动态规划】")

def fibonacci_dp(n):
    """斐波那契 (动态规划)"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

print("斐波那契 (动态规划):")
for i in range(8):
    print(f"  fib({i}) = {fibonacci_dp(i)}")

# 【图的基本操作】
print("\n【7. 图的基本操作】")

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        """添加边"""
        self.graph[u].append(v)
    
    def bfs(self, start):
        """广度优先搜索"""
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        print(f"  BFS 遍历顺序: ", end="")
        while queue:
            vertex = queue.popleft()
            print(f"{vertex} ", end="")
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()
    
    def dfs(self, start, visited=None):
        """深度优先搜索"""
        if visited is None:
            visited = set()
            print(f"  DFS 遍历顺序: ", end="")
        
        visited.add(start)
        print(f"{start} ", end="")
        
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

g = Graph()
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
for u, v in edges:
    g.add_edge(u, v)

print("图的遍历:")
g.bfs("A")
g.dfs("A")
print()

# 【实用案例】
print("\n【8. 实用案例】")

# 案例: 排序和搜索性能对比
print("\n案例: 排序性能对比")

import random

test_size = 1000
test_data = [random.randint(1, 10000) for _ in range(test_size)]

# 快速排序
start = time.time()
quick_sort(test_data.copy())
quick_time = time.time() - start

# Python 内置 sorted
start = time.time()
sorted(test_data)
sorted_time = time.time() - start

print(f"排序 {test_size} 个元素:")
print(f"  快速排序: {quick_time:.6f} 秒")
print(f"  sorted(): {sorted_time:.6f} 秒")

# 案例: 数据去重和排序
print("\\n案例: 数据去重和排序")
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique_sorted = sorted(set(data))
print(f"  原数据: {data}")
print(f"  去重后排序: {unique_sorted}")

# 案例: 查找最频繁的元素
print("\\n案例: 查找最频繁的元素")
from collections import Counter
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
most_common = counter.most_common(2)
print(f"  数据: {data}")
print(f"  最频繁的 2 个元素:")
for item, count in most_common:
    print(f"    {item}: {count} 次")

print("\n✅ 数据结构和算法学习完成！\n")
