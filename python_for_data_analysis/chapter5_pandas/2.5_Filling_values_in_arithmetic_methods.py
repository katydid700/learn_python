# coding=utf-8
"""在算术方法中填充值
也许你希望当一个对象中的某个轴标签在另一个对象中找不到时填充一个特殊值
"""
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.arange(12.).reshape(3, 4), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape(4, 5), columns=list('abcde'))

print(df1 + df2)
"使用add可以填充值"
print(df1.add(df2, fill_value=0))

"灵活的算术方法"
"""
add : 用于加法的方法
sub : 用于减法的方法
div : 用于除法的方法 
mul : 用于乘法的方法
"""