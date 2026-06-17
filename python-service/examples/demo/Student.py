#!/usr/bin/env python3
import json


class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def __show__(self):
        print(f"name:{self.name},age:{self.age},score:{self.score}")

    def __str__(self):
        return json.dumps(self.__dict__)