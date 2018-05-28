# coding=UTF-8
"""函数的参数
在定义函数时给定的名称称作"形参"parameters
在调用函数时由你所提供给函数的值称作"实参"arguments

"""
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b ,'is maximum')

print_max(3,4)