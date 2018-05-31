# coding=utf-8
"""DataFrame和Series之间的运算

"""
import numpy as np
import pandas as pd
"先计算一个二维数组于其某行之间的差"
arr = np.arange(12.).reshape(3, 4)
print(arr - arr[0])
"上面这个就是广播(broadcasting)"
"DataFrame和Series之间的运算也差不多 "
frame = pd.DataFrame(np.arange(12.).reshape(4, 3), columns=list('bde'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
series = frame.ix[0]
print(series)
print(frame - series)