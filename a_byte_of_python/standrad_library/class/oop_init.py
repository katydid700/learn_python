# coding=utf-8
"""__init__
__init__ 方法会在类的对象被实例化（Instantiated）时立即运行。
这一方法可以对任何你想进行操作的目标对象进行初始化（Initialization）操作
"""

class Person:
    def __init__(self, name, ku):
        self.name = name
        self.ku = ku
    def say_hi(self):
        print('hello, my name is ', self.name)

    def namelist(self):
        self.ku = []
        aa = self.ku.append(self.name)
        print(self.ku)
p = Person('Louis','ll')
p.say_hi()
p.namelist()

"""
我们定义一个接受 name 参数的 __init__ 方法
我们创建了一个字段，同样称为 name 。
但是这不是两个相同的变量
当我们在 Person 类下创建新的实例 p 时
先写类的名称再跟括号中加参数: p = Person('Louis')

"""