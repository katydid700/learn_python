# coding=utf-8
"""带有重复值的索引

"""
import numpy as np
import pandas as pd

obj = pd.Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj)

"""
数据选取时,如果是多个,则返回一个Series
否则返回一个标量值
DataFrame 也是如此
"""