# coding=utf-8
"""数组转置和轴对换
转置(transpose)返回源数据的视图
"""
import numpy as np

arr = np.arange(15).reshape(3, 5)
print(arr)
print arr.T

"利用np.dot计算矩阵内积X^T X"
arr1 = np.random.randn(6, 3)
print np.dot(arr1.T, arr1)

"对于高维数组,transpose需要由轴编号组成的元组来转置"
arr2 = np.arange(16).reshape(2, 2, 4)
print(arr2)
print arr2.transpose(1, 0, 2)

"swapaxes"
arr3 = np.arange(16).reshape(2, 2, 4)
print(arr3)
print(arr3.swapaxes(1,2))