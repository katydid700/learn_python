# coding=utf-8
"""丢弃指定轴上的项

"""
import numpy as np
import pandas as pd

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
print(new_obj)

"对于DataFrame 可以删除任意轴上的索引值"
data = pd.DataFrame(np.arange(16).reshape(4, 4), index= ['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data.drop(['Colorado', 'Ohio']))
print(data.drop('two', axis=1))