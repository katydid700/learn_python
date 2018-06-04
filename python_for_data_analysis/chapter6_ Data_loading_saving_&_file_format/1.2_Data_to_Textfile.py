# coding=utf-8
"""将数据写到文本格式

"""
import numpy as np
import pandas as pd
import sys

data = pd.read_csv('ch06/ex5.csv')
"用DataFrame 的 to_csv 方法,将数据写到一个以逗号分隔的文件中"
data.to_csv('ch06/ex5_out.csv')
"sep 参数可以修改分隔符"

"na_rep : 可以将缺失值表示为别的标记值"
# data.to_csv(sys.stout, na_rep='Null')

"Series 也有to_csv的方法"
datas = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=datas)
ts.to_csv('ch06/tseries.csv')

"from_csv : 将csv文件读取为Series"
"上函数已经失效"
cdata = pd.Series.from_csv('ch06/tseries.csv', parse_dates=True)
print(cdata)