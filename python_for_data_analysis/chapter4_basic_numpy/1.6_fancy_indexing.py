# coding=utf-8
"""花式索引
利用整数数组进行索引
与切片不一样,会将数据复制到新数组
"""
import numpy as np

arr = np.empty((8,4))
for i in range(8):
    arr[i] = i

print(arr)
"以特定顺序选取行子集," \
"只需要传入一个用于指定顺序的整数列表或者ndarray即可"
print(arr[[4, 3, 0, 6]])
print(arr[[-4, -3, 0, -6]])

arr = np.arange(32).reshape(8,4)
print(arr)

print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
"若要矩阵形式"
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
"or"
print(arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])