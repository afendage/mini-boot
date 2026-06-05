#!/usr/bin/env python3
"""
案例 15: 综合项目 - 学生管理系统
集成所有学习内容的实际应用
"""

import json
import os
from datetime import datetime

print("=" * 60)
print("案例 15: 综合项目 - 学生管理系统")
print("=" * 60)

class Student:
    """学生类"""
    def __init__(self, student_id, name, age, major, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.gpa = gpa
        self.courses = []
    
    def add_course(self, course):
        """添加课程"""
        if course not in self.courses:
            self.courses.append(course)
    
    def __str__(self):
        return f"学生 {self.name} (ID: {self.student_id}, 年龄: {self.age}, 专业: {self.major}, GPA: {self.gpa})"
    
    def to_dict(self):
        """转为字典"""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "gpa": self.gpa,
            "courses": self.courses
        }

class Course:
    """课程类"""
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits
        self.students = []
    
    def add_student(self, student_id, student_name):
        """添加学生"""
        self.students.append({"student_id": student_id, "name": student_name})
    
    def __str__(self):
        return f"课程 {self.name} (ID: {self.course_id}, 学分: {self.credits})"

class StudentManagementSystem:
    """学生管理系统"""
    def __init__(self, data_file="students_data.json"):
        self.students = {}
        self.courses = {}
        self.data_file = data_file
        self.load_data()
    
    def add_student(self, student_id, name, age, major, gpa):
        """添加学生"""
        if student_id in self.students:
            print(f"  ❌ 学号 {student_id} 已存在")
            return False
        
        student = Student(student_id, name, age, major, gpa)
        self.students[student_id] = student
        print(f"  ✅ 学生 {name} 添加成功")
        return True
    
    def add_course(self, course_id, name, credits):
        """添加课程"""
        if course_id in self.courses:
            print(f"  ❌ 课程 {course_id} 已存在")
            return False
        
        course = Course(course_id, name, credits)
        self.courses[course_id] = course
        print(f"  ✅ 课程 {name} 添加成功")
        return True
    
    def enroll_student(self, student_id, course_id):
        """学生选课"""
        if student_id not in self.students:
            print(f"  ❌ 学号 {student_id} 不存在")
            return False
        
        if course_id not in self.courses:
            print(f"  ❌ 课程 {course_id} 不存在")
            return False
        
        student = self.students[student_id]
        course = self.courses[course_id]
        
        student.add_course(course.name)
        course.add_student(student_id, student.name)
        print(f"  ✅ 学生 {student.name} 成功选课 {course.name}")
        return True
    
    def get_student_info(self, student_id):
        """获取学生信息"""
        if student_id not in self.students:
            print(f"  ❌ 学号 {student_id} 不存在")
            return None
        
        student = self.students[student_id]
        return student
    
    def list_all_students(self):
        """列出所有学生"""
        if not self.students:
            print("  没有学生数据")
            return
        
        for student_id, student in sorted(self.students.items()):
            print(f"  {student}")
    
    def list_all_courses(self):
        """列出所有课程"""
        if not self.courses:
            print("  没有课程数据")
            return
        
        for course_id, course in sorted(self.courses.items()):
            enrolled = len(course.students)
            print(f"  {course} - 已注册: {enrolled} 名学生")
    
    def get_students_by_major(self, major):
        """按专业获取学生"""
        result = [s for s in self.students.values() if s.major == major]
        if not result:
            print(f"  没有找到专业为 {major} 的学生")
            return []
        
        print(f"  专业 {major} 的学生:")
        for student in result:
            print(f"    {student.name} (GPA: {student.gpa})")
        return result
    
    def get_top_students(self, n=3):
        """获取成绩最好的学生"""
        top = sorted(self.students.values(), key=lambda x: x.gpa, reverse=True)[:n]
        print(f"  GPA 最高的 {n} 名学生:")
        for i, student in enumerate(top, 1):
            print(f"    {i}. {student.name} - GPA: {student.gpa}")
        return top
    
    def get_course_enrollment(self, course_id):
        """获取课程注册人数"""
        if course_id not in self.courses:
            print(f"  ❌ 课程 {course_id} 不存在")
            return None
        
        course = self.courses[course_id]
        print(f"  课程 {course.name} 已注册学生:")
        for student in course.students:
            print(f"    - {student['name']} (ID: {student['student_id']})")
        return course.students
    
    def calculate_average_gpa(self):
        """计算平均 GPA"""
        if not self.students:
            return 0
        
        total_gpa = sum(s.gpa for s in self.students.values())
        avg_gpa = total_gpa / len(self.students)
        return avg_gpa
    
    def save_data(self):
        """保存数据到文件"""
        data_dir = "d:\\work\\projects\\figer\\python-service\\sample_files"
        os.makedirs(data_dir, exist_ok=True)
        
        file_path = os.path.join(data_dir, self.data_file)
        
        data = {
            "students": {sid: s.to_dict() for sid, s in self.students.items()},
            "courses": {
                cid: {
                    "course_id": c.course_id,
                    "name": c.name,
                    "credits": c.credits,
                    "students": c.students
                }
                for cid, c in self.courses.items()
            },
            "saved_at": datetime.now().isoformat()
        }
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  ✅ 数据已保存到 {file_path}")
            return True
        except Exception as e:
            print(f"  ❌ 保存失败: {e}")
            return False
    
    def load_data(self):
        """从文件加载数据"""
        data_dir = "d:\\work\\projects\\figer\\python-service\\sample_files"
        file_path = os.path.join(data_dir, self.data_file)
        
        if not os.path.exists(file_path):
            return False
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 加载学生
            for sid, sdata in data.get("students", {}).items():
                student = Student(sdata["student_id"], sdata["name"], 
                                sdata["age"], sdata["major"], sdata["gpa"])
                student.courses = sdata.get("courses", [])
                self.students[sid] = student
            
            # 加载课程
            for cid, cdata in data.get("courses", {}).items():
                course = Course(cdata["course_id"], cdata["name"], cdata["credits"])
                course.students = cdata.get("students", [])
                self.courses[cid] = course
            
            print(f"  ✅ 数据已从文件加载")
            return True
        except Exception as e:
            print(f"  ❌ 加载失败: {e}")
            return False
    
    def generate_report(self):
        """生成报告"""
        print("\n" + "=" * 50)
        print("学生管理系统 - 统计报告")
        print("=" * 50)
        
        print(f"\\n总学生数: {len(self.students)}")
        print(f"总课程数: {len(self.courses)}")
        print(f"平均 GPA: {self.calculate_average_gpa():.2f}")
        
        if self.students:
            majors = set(s.major for s in self.students.values())
            print(f"\\n学生专业分布:")
            for major in majors:
                count = len([s for s in self.students.values() if s.major == major])
                print(f"  {major}: {count} 人")
        
        if self.courses:
            print(f"\\n课程注册情况:")
            for course_id, course in self.courses.items():
                print(f"  {course.name}: {len(course.students)} 人")

# 【系统演示】
print("\n【系统演示】\n")

# 初始化系统
system = StudentManagementSystem()

# 添加学生
print("1. 添加学生:")
system.add_student("001", "张三", 20, "计算机科学", 3.8)
system.add_student("002", "李四", 21, "软件工程", 3.6)
system.add_student("003", "王五", 20, "计算机科学", 3.9)
system.add_student("004", "赵六", 22, "数据科学", 3.7)
system.add_student("005", "孙七", 21, "软件工程", 3.5)

# 添加课程
print("\\n2. 添加课程:")
system.add_course("C001", "Python 编程", 3)
system.add_course("C002", "数据结构", 4)
system.add_course("C003", "数据库", 3)
system.add_course("C004", "Web 开发", 3)

# 学生选课
print("\\n3. 学生选课:")
system.enroll_student("001", "C001")
system.enroll_student("001", "C002")
system.enroll_student("002", "C001")
system.enroll_student("002", "C003")
system.enroll_student("003", "C001")
system.enroll_student("003", "C004")
system.enroll_student("004", "C002")
system.enroll_student("005", "C003")

# 列出所有学生
print("\\n4. 所有学生:")
system.list_all_students()

# 列出所有课程
print("\\n5. 所有课程:")
system.list_all_courses()

# 按专业查询
print("\\n6. 按专业查询:")
system.get_students_by_major("计算机科学")

# GPA 最高的学生
print("\\n7. GPA 最高的学生:")
system.get_top_students(3)

# 课程注册情况
print("\\n8. 课程注册情况:")
system.get_course_enrollment("C001")

# 生成报告
system.generate_report()

# 保存数据
print("\\n9. 保存数据:")
system.save_data()

print("\n✅ 综合项目学习完成！\n")
print("=" * 60)
