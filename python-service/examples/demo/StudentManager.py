#!/usr/bin/env python3
from examples.demo.Student import Student


class StudentManager:


    def __init__(self):
        self.students = []

    def add(self):
        name = input("input your name：")
        age = int(input("input your age："))
        score = float(input("input your score："))
        stu = Student(name, age, score)

        self.students.append(stu)
        print(f"add success stu:{stu}")


    def delete(self):
        name = input("input your name:")
        for stu in self.students:
            if name == stu.name:
                self.students.remove(stu)
                print("delete success")
                return
        print("no exits the student")


    def update(self):
        name = input("select you need update name:")
        updName = input("input your new name:")
        for stu in self.students:
            if name == stu.name:
                stu.name = updName
                print("update success")
                return
        print("no exits the student")


    def query(self):
        if len(self.students) == 0:
            print("no student")
            return
        for stu in self.students:
            stu.__show__()
            print("\n")


    def menu(self):
        while True:
            print("\n")
            print("=" * 8 + "this is my students manager system" + "=" * 8)
            print("1.add student")
            print("2.delete student")
            print("3.update student")
            print("4.query student")
            print("0.exit")

            choice = input("input your choice:")
            if choice == "1":
                self.add()
            elif choice == "2":
                self.delete()
            elif choice == "3":
                self.update()
            elif choice == "4":
                self.query()
            elif choice == "0":
                print("bye bye")
                break
            else:
                print("input error")


if __name__ == "__main__":
    stuManager = StudentManager()
    stuManager.menu()
