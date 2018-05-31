# coding=utf-8
"""重新索引
创建一个适应新索引的新对象
"""
import pandas as pd
import numpy as np

obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
print(obj)
"利用reindex对Series进行重排" \
"fill_value : 引入缺失值"
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=1)
print(obj2)

"ffill : 实现前向值填充"
obj3 = pd.Series(['blue', 'purple', 'yellow'], index= [0, 2, 4])
obj4 = obj3.reindex(range(6), method='ffill')
print(obj4)
"reindex 的插值method选项"
"""
ffill / pad : 前向填充值
bfill / backfill : 后向填充值
"""

"reindex 函数的参数"
"""
index : 用作索引的新序列
method : 插值方式
fill_value : 重新索引过程中,引入缺失值
limit : 前向或后向填充时的最大填充值
level : 在MultiIndex的指定级别上匹配简单索引
copy : 默认为True, 无论如何都复制;如果为False , 新旧相等则不复制
"""