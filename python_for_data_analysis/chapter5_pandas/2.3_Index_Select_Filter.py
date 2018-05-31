# coding=utf-8
"""索引 选取 过滤

"""
import numpy as np
import pandas as pd

"Series 的索引类似于Numpy数组的索引,只不过不是整数"
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj['b'])
print(obj[1])
print(obj[2:4])
print(obj[['b', 'a', 'd']])
print(obj[[1, 3]])
print(obj[obj < 2])
"利用标签的切片运算于普通的python切片运算不同,其末端是包含的"
print(obj['b':'d'])

"DataFrame 的索引就是获取一个或多个列"
data = pd.DataFrame(np.arange(16).reshape(4,4),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
print(data['two'])
print(data[['three', 'one']])
print(data[:2])
print(data[data['three'] > 5])

"DataFrame 的索引选项"
"""
obj[val] : 选取DataFrame的单个或一组列,
obj.ix[val] : 选取DataFrame的单个或一组行
obj.ix[:, val] : 选取单个或一组列
obj.ix[val1, val2] : 同时选取行和列
reindex方法 : 将一个或多个轴匹配到新索引
xs方法 : 根据标签选取单行或单列,并返回一个Series
icol、irow方法 : 根据整数位置选取单列或单行,并返回一个Series
get_value、set_value方法 : 根据行标签和列标签选取单个值
"""