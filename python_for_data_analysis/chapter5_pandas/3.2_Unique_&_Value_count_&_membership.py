# coding=utf-8
"""唯一值 值计数 成员资格

"""
import numpy as np
import pandas as pd

obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c'])
print(obj.unique())

"唯一值 值计数 成员资格 的方法"
"""
isin : 计算一个表示'Series各值是否包含于传入的值序列中'的布尔型数组
value_counts : 计算一个Series 中各值出现的频率
                还是一个pandas顶级方法,可以用于任何数组或序列
unique : 计算Series中的唯一值数组,按发现的顺序返回
"""
print(obj.isin(['b', 'c']))
print(obj.value_counts())
"返回一个相关列的柱状图"
data = pd.DataFrame({1: [1, 3, 4, 3, 4],
                     2: [2, 3, 1, 2, 3],
                     3: [1, 5, 2, 4, 4]})
print data.apply(pd.value_counts).fillna(0)


