# coding=utf-8
"""数组和标量的运算
大小相等的数组之间的任何运算都会应用到元素级
数组与标量的运算也会传播到各个元素
"""
import numpy as np

arr = np.array([[1., 2., 3. ], [4., 5., 6. ]])
print(arr * arr)
print(arr - arr)
arr1 = 1/arr
print(arr1)
print(arr ** 0.5)