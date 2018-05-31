# coding=utf-8
"""填充缺失数据

"""
import numpy as np
import pandas as pd
from numpy import nan as NA


df = pd.DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
print(df)
print(df.fillna(0))
"传入dict 则有不同的变化"
print(df.fillna({1: 0.5, 2: -1}))
"fillna(inplace=True) : 表示原地修改,否则建立一个新的对象"

"fillna函数的参数"
"""
value : 用于填充缺失值的标量值或字典对象
method : 插值方式,默认ffill
axis : 待填充的轴
inplace : 修改调用者对象而不产生副本
limit : 可以连续填充的最大数量
"""