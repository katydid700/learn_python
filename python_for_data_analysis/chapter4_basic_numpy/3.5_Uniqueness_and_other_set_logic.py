# coding=utf-8
"""唯一化以及其他的集合逻辑

"""
import  numpy as np

"unique : 用于找出数组中的唯一值并返回已排序的结果"

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))

"intersect1d(x,y) : 计算x和y中的公共元素,并返回有序结果"

"union1d(x,y) : 计算x和y的并集, 并返回有序结果"

"in1d(x,y) : 得到一个'x中是否有y的元素'的布尔型数组"
values = np.array([6, 0, 0, 3, 2, 5, 6])
print(np.in1d(values, [2, 3, 6]))

"setdiff1d(x,y) : 集合的差, 在x且不在y中的元素"

"setxor1d(x,y) : 存在一个数组但不同时存在于两个数组"

