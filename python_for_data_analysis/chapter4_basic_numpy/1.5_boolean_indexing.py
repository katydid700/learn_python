# coding=utf-8
"""布尔型索引
布尔型数组的长度必须跟被索引的轴长度一致
"""
import numpy as np

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7,4)

print names == 'Bob'
print(data[names == 'Bob'])

print(data[names == 'Bob', 2:])

"选用其他值可以用!= "
print(data[names != 'Bob'])

"也可以组合两个人或多个人, 但是and 和 or 无效"
print(data[(names == 'Bob') | (names == 'Will')])