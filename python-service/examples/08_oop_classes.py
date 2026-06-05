#!/usr/bin/env python3
"""
案例 08: 面向对象编程 (OOP)
知识点：
  - 类和对象
  - 属性和方法
  - 初始化方法 (__init__)
  - 继承
  - 多态
  - 特殊方法 (__str__, __repr__, 等)
"""

print("=" * 60)
print("案例 08: 面向对象编程 (OOP)")
print("=" * 60)

# 【类和对象】
print("\n【1. 类和对象】")

class Dog:
    """狗类"""
    
    # 类属性
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """初始化方法"""
        # 实例属性
        self.name = name
        self.age = age
    
    def bark(self):
        """狗叫的方法"""
        print(f"  {self.name}: 汪汪汪！")
    
    def describe(self):
        """描述狗的信息"""
        print(f"  {self.name} 是一只 {self.age} 岁的 {self.species}")

# 创建对象 (实例)
dog1 = Dog("小黄", 3)
dog2 = Dog("小白", 5)

print(f"dog1.name = {dog1.name}")
print(f"dog1.age = {dog1.age}")
print(f"Dog.species = {Dog.species}")

print("\\n调用方法:")
dog1.bark()
dog2.describe()

# 【特殊方法】
print("\n【2. 特殊方法】")

class Person:
    """人类"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """返回用户友好的字符串表示"""
        return f"{self.name} ({self.age}岁)"
    
    def __repr__(self):
        """返回正式的字符串表示"""
        return f"Person('{self.name}', {self.age})"
    
    def __eq__(self, other):
        """判断是否相等"""
        if not isinstance(other, Person):
            return False
        return self.name == other.name and self.age == other.age
    
    def __lt__(self, other):
        """小于比较"""
        return self.age < other.age
    
    def __len__(self):
        """返回名字长度"""
        return len(self.name)

p1 = Person("张三", 25)
p2 = Person("李四", 30)
p3 = Person("张三", 25)

print(f"str(p1) = {str(p1)}")  # __str__
print(f"repr(p1) = {repr(p1)}")  # __repr__
print(f"p1 == p3 = {p1 == p3}")  # __eq__
print(f"p1 < p2 = {p1 < p2}")  # __lt__
print(f"len(p1) = {len(p1)}")  # __len__

# 【属性和方法】
print("\n【3. 属性和方法】")

class Student:
    """学生类"""
    
    def __init__(self, name, score):
        self.name = name
        self._score = score  # 受保护的属性 (约定)
        self.__private = "私有属性"  # 私有属性
    
    # 实例方法
    def study(self, subject):
        print(f"  {self.name} 正在学习 {subject}")
    
    # 类方法
    @classmethod
    def from_string(cls, info):
        """从字符串创建对象"""
        name, score = info.split(",")
        return cls(name, int(score))
    
    # 静态方法
    @staticmethod
    def is_pass(score):
        """判断是否及格"""
        return score >= 60
    
    # 属性 (getter)
    @property
    def score(self):
        return self._score
    
    # 属性 (setter)
    @score.setter
    def score(self, value):
        if 0 <= value <= 100:
            self._score = value
        else:
            raise ValueError("成绩必须在 0-100 之间")
    
    # 属性 (deleter)
    @score.deleter
    def score(self):
        print(f"  删除 {self.name} 的成绩")
        del self._score

print("实例方法:")
student = Student("王五", 85)
student.study("Python")

print("\\n类方法:")
student2 = Student.from_string("赵六,90")
print(f"  {student2.name}: {student2.score}")

print("\\n静态方法:")
print(f"  Student.is_pass(85) = {Student.is_pass(85)}")
print(f"  Student.is_pass(50) = {Student.is_pass(50)}")

print("\\n属性:")
print(f"  student.score = {student.score}")
student.score = 95
print(f"  修改后: student.score = {student.score}")

# 【继承】
print("\n【4. 继承】")

class Animal:
    """动物类 (父类)"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print(f"  {self.name} 发出声音")
    
    def move(self):
        print(f"  {self.name} 在移动")

class Cat(Animal):
    """猫类 (子类)"""
    
    def make_sound(self):
        """重写父类方法"""
        print(f"  {self.name}: 喵喵喵")

class Dog(Animal):
    """狗类 (子类)"""
    
    def make_sound(self):
        """重写父类方法"""
        print(f"  {self.name}: 汪汪汪")
    
    def fetch(self):
        """独有的方法"""
        print(f"  {self.name} 叼回了球")

cat = Cat("小猫")
dog = Dog("小狗")

print("多态:")
cat.make_sound()
cat.move()
dog.make_sound()
dog.fetch()

# 【多重继承】
print("\n【5. 多重继承】")

class Flyable:
    """可飞行的混入类"""
    
    def fly(self):
        print(f"  {self.name} 正在飞")

class Swimmable:
    """可游泳的混入类"""
    
    def swim(self):
        print(f"  {self.name} 正在游泳")

class Duck(Flyable, Swimmable):
    """鸭子类 (多重继承)"""
    
    def __init__(self, name):
        self.name = name

duck = Duck("唐老鸭")
duck.fly()
duck.swim()
print(f"  Duck 的 MRO: {[cls.__name__ for cls in Duck.__mro__]}")

# 【super() 和 super 调用】
print("\n【6. super() 调用父类方法】")

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"  {self.brand} 车启动")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # 调用父类初始化
        self.model = model
    
    def start(self):
        super().start()  # 调用父类方法
        print(f"  准备驾驶 {self.model}")

car = Car("宝马", "X5")
car.start()

# 【实用案例】
print("\n【7. 实用案例】")

# 案例: 银行账户系统
print("\\n案例: 银行账户系统")

class Account:
    """银行账户"""
    
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self._balance += amount
            print(f"  ✅ {self.owner} 存入 {amount} 元，余额: {self._balance}")
        else:
            print(f"  ❌ 存款金额必须大于 0")
    
    def withdraw(self, amount):
        """取款"""
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"  ✅ {self.owner} 取出 {amount} 元，余额: {self._balance}")
        else:
            print(f"  ❌ 取款金额无效")
    
    def transfer(self, other_account, amount):
        """转账"""
        if amount > 0 and amount <= self._balance:
            self.withdraw(amount)
            other_account.deposit(amount)
            print(f"  ✅ 转账完成")
        else:
            print(f"  ❌ 转账失败")

class SavingsAccount(Account):
    """储蓄账户 (子类)"""
    
    def __init__(self, account_number, owner, balance=0, interest_rate=0.02):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        """添加利息"""
        interest = self._balance * self.interest_rate
        self.deposit(interest)
        print(f"  利息已添加")

print("创建账户:")
acc1 = Account("001", "张三", 1000)
acc2 = SavingsAccount("002", "李四", 2000, 0.03)

print("\\n操作账户:")
acc1.deposit(500)
acc1.withdraw(200)
acc1.transfer(acc2, 300)
acc2.add_interest()

print(f"\\n张三账户余额: {acc1.balance}")
print(f"李四账户余额: {acc2.balance}")

print("\n✅ 面向对象编程学习完成！\n")
