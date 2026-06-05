#!/usr/bin/env python3
"""
案例 11: 装饰器 (Decorators)
知识点：
  - 装饰器的基本概念
  - 编写简单装饰器
  - 带参数的装饰器
  - 装饰器的应用场景
"""

import time
import functools

print("=" * 60)
print("案例 11: 装饰器 (Decorators)")
print("=" * 60)

# 【装饰器基础】
print("\n【1. 装饰器基础】")

# 装饰器是一个函数，接收一个函数作为参数，返回一个新函数
def my_decorator(func):
    """简单的装饰器"""
    def wrapper():
        print("  执行前")
        func()
        print("  执行后")
    return wrapper

@my_decorator
def say_hello():
    print("  Hello!")

print("调用被装饰的函数:")
say_hello()

# 【装饰器传递参数】
print("\n【2. 装饰器传递参数】")

def decorator_with_args(func):
    """可以处理函数参数的装饰器"""
    def wrapper(*args, **kwargs):
        print(f"  参数: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  返回值: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

print("调用 add(5, 3):")
add(5, 3)

# 【带参数的装饰器】
print("\n【3. 带参数的装饰器】")

def repeat(times):
    """重复执行函数的装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    return f"Hello, {name}!"

print("调用 greet('Alice') (重复 3 次):")
results = greet("Alice")
for r in results:
    print(f"  {r}")

# 【保留函数元数据】
print("\n【4. 保留函数元数据 (functools.wraps)】")

def before_functools(func):
    """不使用 functools.wraps"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def with_functools(func):
    """使用 functools.wraps"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@before_functools
def func_without_wraps():
    """这是原始函数文档"""
    pass

@with_functools
def func_with_wraps():
    """这是原始函数文档"""
    pass

print(f"不使用 functools.wraps:")
print(f"  __name__: {func_without_wraps.__name__}")
print(f"  __doc__: {func_without_wraps.__doc__}")

print(f"\\n使用 functools.wraps:")
print(f"  __name__: {func_with_wraps.__name__}")
print(f"  __doc__: {func_with_wraps.__doc__}")

# 【性能监测装饰器】
print("\n【5. 性能监测装饰器】")

def timer(func):
    """测量函数执行时间的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"  {func.__name__} 执行时间: {execution_time:.6f} 秒")
        return result
    return wrapper

@timer
def slow_function():
    """模拟一个缓慢的函数"""
    time.sleep(0.1)
    return "完成"

print("调用 slow_function():")
result = slow_function()

# 【日志装饰器】
print("\n【6. 日志装饰器】")

def log_calls(func):
    """记录函数调用的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  🔍 调用 {func.__name__}")
        print(f"    参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"    返回: {result}")
        return result
    return wrapper

@log_calls
def multiply(x, y):
    return x * y

print("调用 multiply(5, 3):")
multiply(5, 3)

# 【验证装饰器】
print("\n【7. 验证装饰器】")

def validate_positive(*arg_names):
    """验证参数为正数的装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for name, value in zip(arg_names, args):
                if not isinstance(value, (int, float)) or value < 0:
                    raise ValueError(f"{name} 必须是正数")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_positive("a", "b")
def divide(a, b):
    return a / b

print("调用 divide(10, 2):")
print(f"  结果: {divide(10, 2)}")

print("\\n调用 divide(-5, 2) (应该报错):")
try:
    divide(-5, 2)
except ValueError as e:
    print(f"  ❌ {e}")

# 【多个装饰器】
print("\n【8. 多个装饰器](#")

def uppercase(func):
    """转大写的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def add_exclamation(func):
    """添加感叹号的装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@add_exclamation
@uppercase
def greet_name(name):
    return f"hello, {name}"

print("多个装饰器应用:")
print(f"  {greet_name('alice')}")

# 【类装饰器】
print("\n【9. 类装饰器】")

class CountCalls:
    """统计函数调用次数的装饰器 (类)"""
    def __init__(self, func):
        self.func = func
        self.call_count = 0
    
    def __call__(self, *args, **kwargs):
        self.call_count += 1
        print(f"  函数被调用了 {self.call_count} 次")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    return "Hi!"

print("使用类装饰器:")
say_hi()
say_hi()
say_hi()
print(f"总调用次数: {say_hi.call_count}")

# 【实用案例】
print("\n【10. 实用案例】")

# 案例1: 缓存装饰器
print("\n案例1: 缓存装饰器 (Memoization)")

def cache(func):
    """缓存函数结果的装饰器"""
    cached_results = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"  使用缓存的结果")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    
    return wrapper

@cache
def fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("第一次计算 fibonacci(10):")
start = time.time()
result = fibonacci(10)
print(f"  结果: {result}, 耗时: {(time.time()-start):.6f}秒")

print("\\n第二次计算 fibonacci(10):")
start = time.time()
result = fibonacci(10)
print(f"  结果: {result}, 耗时: {(time.time()-start):.6f}秒")

# 案例2: 重试装饰器
print("\n案例2: 重试装饰器")

def retry(max_attempts=3):
    """如果函数失败，重新尝试的装饰器"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    print(f"  尝试第 {attempt} 次...")
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        print(f"  ❌ 全部失败: {e}")
                        raise
                    print(f"  失败: {e}，准备重试...")
            return None
        return wrapper
    return decorator

call_count = 0

@retry(3)
def unstable_function():
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("连接失败")
    return "成功!"

print("调用不稳定的函数:")
try:
    result = unstable_function()
    print(f"  结果: {result}")
except Exception as e:
    print(f"  最终失败: {e}")

print("\n✅ 装饰器学习完成！\n")
