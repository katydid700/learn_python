# coding=utf-8
"""使用DataFrame的列

"""
import numpy as np
import pandas as pd

frame = pd.DataFrame({'a': range(7),
                      'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame)

"set_index : 将一个或多个列转为行索引,并创建一个新的DataFrame"
frame2 = frame.set_index(['c', 'd'])
print(frame2)
"reset_index : 与上述相反,层次化索引的级别会被转移到列里面"
