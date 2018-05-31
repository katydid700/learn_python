# coding=utf-8
"""滤除缺失数据

"""

import numpy as np
import pandas as pd
from numpy import nan as NA

data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())
print(data[data.notnull()])

"对于DataFrame, dropna 默认丢弃任何含有缺失值的行"
data1 = pd.DataFrame([[1. ,6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])
print(data1.dropna())
"传入 how='all'  则之丢弃全是NA的"
print(data1.dropna(how='all'))
"丢弃列 只需要传入 axis=1 即可"

"thresh  :  "