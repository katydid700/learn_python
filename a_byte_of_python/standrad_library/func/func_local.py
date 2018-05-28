# coding=UTF-8
"""局部变量
当你在一个函数的定义中申明变量时,它们不会以任何方式与函数之外但具有相同名称的变量产生关系,
即这些变量属于局部变量
"""

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('changed local x to ', x)

func(x)
print('x is still ', x)