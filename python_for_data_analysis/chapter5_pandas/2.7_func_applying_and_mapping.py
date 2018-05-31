# coding=utf-8
"""函数应用和映射

"""
import numpy as np
import pandas as pd

"Numpy 的ufuncs方法可以用于操作pandas对象"
frame = pd.DataFrame(np.arange(12.).reshape(4, 3), columns=list('bed'),
                     index=['Utah', 'Ohio', 'Texas', 'Oregon'])
print(np.abs(frame))

"apply : 将函数应用到由各列或各行所形成的一维数组上"
f = lambda x: x.max() - x.min()
print frame.apply(f)
print(frame.apply(f, axis=1))
"applymap : 可以应用到元素级"
"Series 有一个应用元素级函数的map方法"