# coding=utf-8
"""算术运算和数据对齐
Pandas最重要的功能在于
可以对不同索引的对象进行算术运算
"""
import numpy as np
import pandas as pd
"如果对象相加,存在不同索引,则结果即为并集"
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1 + s2)


"对于DataFrame,对齐操作会同时发生在行和列上"
df1 = pd.DataFrame(np.arange(9.).reshape(3, 3), columns=list('bcd'), index=['Ohio', 'Texas', 'Colorado'])
df2 = pd.DataFrame(np.arange(12.).reshape(4, 3), columns=list('bde'), index=['Utah', 'Ohio', 'Texas', 'Oregon'])

print(df1 + df2)