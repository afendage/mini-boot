#!/usr/bin/env python3
"""
Python 学习案例 - 主程序
运行这个程序来选择和执行不同的学习案例
"""

import os
import sys
import subprocess

def main():
    examples = {
        "0": ("退出", None),
        "1": ("00_hello.py", "Hello Python - 第一个程序"),
        "2": ("01_variables_and_types.py", "变量和数据类型"),
        "3": ("02_strings.py", "字符串操作和格式化"),
        "4": ("03_lists_and_tuples.py", "列表和元组"),
        "5": ("04_dictionaries_and_sets.py", "字典和集合"),
        "6": ("05_control_flow.py", "控制流 (if/for/while)"),
        "7": ("06_functions.py", "函数"),
        "8": ("07_file_io.py", "文件 I/O 和异常处理"),
        "9": ("08_oop_classes.py", "面向对象编程"),
        "10": ("09_modules_and_imports.py", "模块和导入"),
        "11": ("10_list_comprehension.py", "列表推导式和推导式"),
        "12": ("11_decorators.py", "装饰器"),
        "13": ("12_generators.py", "生成器"),
        "14": ("13_json_handling.py", "JSON 处理"),
        "15": ("14_data_structures.py", "数据结构和算法"),
        "16": ("15_comprehensive_project.py", "综合项目 - 学生管理系统"),
        "17": ("all", "运行所有案例"),
    }
    
    while True:
        print("\\n" + "=" * 60)
        print("Python 学习案例 - 主菜单")
        print("=" * 60)
        print()
        
        for key in sorted(examples.keys()):
            if examples[key][1]:
                print(f"  {key:2s} - {examples[key][1]}")
        
        print()
        choice = input("请选择要运行的案例 (0-17): ").strip()
        
        if choice not in examples:
            print("❌ 无效的选择，请重试")
            continue
        
        if choice == "0":
            print("👋 感谢使用，再见！")
            break
        
        if choice == "17":
            run_all_examples()
        else:
            example_file = examples[choice][0]
            run_example(example_file)
        
        input("\\n按 Enter 键返回菜单...")

def run_example(filename):
    """运行单个案例"""
    examples_dir = os.path.dirname(__file__)
    file_path = os.path.join(examples_dir, filename)
    
    if not os.path.exists(file_path):
        print(f"❌ 文件不存在: {file_path}")
        return
    
    print(f"\\n运行: {filename}\\n")
    print("-" * 60)
    
    try:
        # 在同一个进程中执行，保持输出的连续性
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        exec(code)
    except Exception as e:
        print(f"\\n❌ 执行出错: {e}")
        import traceback
        traceback.print_exc()

def run_all_examples():
    """运行所有案例"""
    examples_dir = os.path.dirname(__file__)
    
    examples = [
        "00_hello.py",
        "01_variables_and_types.py",
        "02_strings.py",
        "03_lists_and_tuples.py",
        "04_dictionaries_and_sets.py",
        "05_control_flow.py",
        "06_functions.py",
        "07_file_io.py",
        "08_oop_classes.py",
        "09_modules_and_imports.py",
        "10_list_comprehension.py",
        "11_decorators.py",
        "12_generators.py",
        "13_json_handling.py",
        "14_data_structures.py",
        "15_comprehensive_project.py",
    ]
    
    print("\\n开始运行所有案例...")
    print("=" * 60)
    
    total = len(examples)
    for i, example in enumerate(examples, 1):
        print(f"\\n[{i}/{total}] 运行: {example}")
        print("-" * 60)
        
        file_path = os.path.join(examples_dir, example)
        if not os.path.exists(file_path):
            print(f"❌ 文件不存在: {file_path}")
            continue
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code)
        except Exception as e:
            print(f"❌ 执行出错: {e}")
        
        # 在每个案例之间添加分隔符
        if i < total:
            print("\\n" + "=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\\n\\n⚠️ 程序被中断")
        sys.exit(0)
