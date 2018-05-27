# coding=UTF-8
"""
从函数中返回,即中断函数
也可以选择在中断函数时从函数中返回一个值
"""
def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal '
    else:
        return y

print(maximum(2,3))

print(max(4,5))