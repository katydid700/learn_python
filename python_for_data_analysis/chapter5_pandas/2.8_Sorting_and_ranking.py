# coding=utf-8
"""排序和排名

"""
import pandas as pd
import numpy as np

obj = pd.Series(range(4), index=['d', 'b', 'c', 'a'])
print(obj.sort_index())

"对于DataFrame 可以根据任意一个轴上的索引进行排序"
frame = pd.DataFrame(np.arange(8).reshape(2, 4), index=['three', 'one'],
                     columns=['d', 'a', 'b', 'c'])
print(frame.sort_index())
print(frame.sort_index(axis=1))
"sort_index(ascending=False) : 降序排序"

"order : 按值对Series进行排序  (这个好像已经失效了)"
# obj2 = pd.Series([4, 7, -4, 3])
# print(obj2.order())

"""by : DataFrame上,根据一个或多个列上的值进行排序
其中by argument to sort_index is deprecated, please use .sort_values(by=...)
"""
frame2 = pd.DataFrame({'b': [4, 7, -4, 3], 'a':[2, 3, 4, 1]})
print(frame2.sort_values(by='b'))
print(frame2.sort_values(by=['a','b']))
"而且并没有同时排序  ???  "

"默认情况下,rank通过'为各组分配一个平均排名'的方式破坏平级关系"

obj2 = pd.Series([7, -5, 7, 4, 2, 0, 4])
print('***********')
print(obj2.rank())
"排名时用于破坏平级关系的method选项"
"""
average : 默认: 在相等分组中,为各个值分配平均排名
min : 使用整个分组的最小排名
max : 使用整个分组的最大排名
first : 按值在原始数据中的出现顺序分配排名
"""