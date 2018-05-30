# coding=utf-8
"""创建n维向量
array函数接受一切序列型的对象
然后产生一个新的含有传入数据的numpy数据

"""
import numpy as np
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
"嵌套序列将会被转为多维数组"
data2 = [[1, 2, 3, 4],[5, 6, 7, 8] ]
arr2 = np.array(data2)
print(arr2)
"维度"
print(arr2.ndim)
"形状"
print(arr2.shape)
"数据类型"
print(arr1.dtype)
print(arr2.dtype)

"全0数组"
print(np.zeros((3,6)))

"0-(n-1)数组"
print(np.arange(1,11))

"单位矩阵"
print(np.eye(3))
print(np.identity(4))