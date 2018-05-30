# coding=utf-8
"""基本的索引和切片
跟列表的主要区别在于:
数组切片是原始数组的视图,
任何修改都会直接反映到原数组上
"""
import  numpy as np
arr = np.arange(10)
arr[5:8] = 12
print(arr)
arr_slice = arr[5:8]
arr_slice[1] = 12345
print(arr)
arr_slice[:] = 64
print(arr)

arr2d = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2][1])
print('arr2d[2][1] == arr2d[2, 1]')
print(arr2d[2, 1])

print(arr2d[:2, 1:])