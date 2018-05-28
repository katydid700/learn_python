# coding=UTF-8
"""
类方法与普通函数只有一种特定的区别——
前者必须多加一个参数在参数列表开头，
这个名字必须添加到参数列表的开头，
但是你不用在你调用这个功能时为这个参数赋值，
Python 会为它提供。
这种特定的变量引用的是对象本身，
按照惯例，它被赋予 self 这一名称。
"""

"""
你一定会在想 Python 是如何给 self 赋值的，以及为什么你不必给它一个值。一个例子或许
会让这些疑问得到解答。假设你有一个 MyClass 的类，这个类下有一个实例 myobject 。当
你调用一个这个对象的方法，如 myobject.method(arg1, arg2) 时，Python 将会自动将其转
换成 MyClass.method(myobject, arg1, arg2) ——这就是 self 的全部特殊之处所在。
"""
class zhu:
    def hi(self):
        print('hello world ')

p = zhu()
p.hi()
zhu().hi()