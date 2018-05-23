# -*- coding: utf-8 -*-
import numpy as np

"""
2.1.1   创建数组
"""
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([[1,2,3,4],
             [4,5,6,7],
             [7,8,9,10]])
"""
显示数组的形状
"""
a.shape
b.shape
c.shape
"""
改变形状 
如果为-1 则自动计算长度
"""
c.shape = 4,3
c.shape = 2,-1
"""
reshape 构建制定形状的新数组,该数组与原数组共享存储空间
"""
d = a.reshape((2,2))
"""
2.1.2   设置元素类型
        修改元素类型
"""
ai32 = np.array([1,2,3,4],dtype = np.int32)
ai64 = ai32.astype(np.complex64)
"""
2.1.3   自动生成数组
"""
a213 = np.arange(0,1,0.1)
"""
linspace 指定开始值\终值\元素个数 , endpoint (true/false) 代表有无终值
"""
b213 = np.linspace(0,1,10,endpoint=True)
c213 = np.linspace(0,1,10,endpoint=False)
"""
logspace 创建等比数列
"""
d213 = np.logspace(0,2,5)
e213 = np.logspace(0,1,12,base=2,endpoint=False)
"""
zeros() 初始化为0数组  ; zeros_like(a) = zeros(a.shape,a.dtype)
ones()  初始化为1数组
"""
f213 = np.ones(4)
g213 = np.zeros(4)

"""
fromfunction
"""
def func2(i,j):
    return (i+1)*(j+1)
h213 = np.fromfunction(func2, (9,9))

"""
2.1.4   存取元素
切片后的数组与原数组享用同一存储空间
使用整数数组时不共享
"""
a214 = np.arange(10)
b214 = a214[-1]
"""
布尔数组
"""
c214 = np.random.randint(0,10,6)
print (c214[c214>5])

"""
2.1.5 多维数组
"""
a215 = np.arange(0, 60, 10).reshape(-1,1) + np.arange(0, 6)