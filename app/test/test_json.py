# -*-coding:utf-8-*-

from app.util import obj2json


class Student:
    """简单的Dto类转JSON示例

    """

    def __init__(self):
        self.name = '张三'
        self.age = 1
        self.hobby = ['羽毛球', '游泳']


student = Student()
print(obj2json(student))
print(obj2json({'name': [1, 2, 3]}))
