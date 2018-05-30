# coding=utf-8
"""排序
一维数组用sort排序
多维数组将轴编号传给sort排序
"""
import numpy as np

arr = np.random.randn(8)
print(arr)
sort_arr  = np.sort(arr)
print(sort_arr)