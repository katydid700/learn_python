# coding=utf-8
"""层次化索引
能使你在一个轴上拥有多个索引级别
"""
import numpy as np
import pandas as pd

data = pd.Series(np.random.randn(10),
                 index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data)
print(data.index)
print(data['b'])

"层次化索引在数据重塑和基于分组的操作中很重要"
"unstack : 把一组数据重新安排到一个DataFrame中"
print(data.unstack())
"stack : 为其逆运算"