# coding=utf-8
"""索引对象
管理轴标签和其他元数据(轴名称等)

"""
import pandas as pd
import numpy as np

obj = pd.Series(range(3), index= ['a', 'b', 'c'])
index = obj.index
print(index)
print(index[1:])
"index 对象是不可修改的"

"pandas 中的主要Index 对象"
"""
Index : 最泛化的Index对象,
Int64Index : 针对整数的特殊Index
MultiIndex : '层次化'索引对象,表示单个轴上的多层索引
DatetimeIndex : 存储纳秒级时间戳
PeriodIndex : 针对Period 数据的特殊Index
"""

"Index的方法和属性"
"""
append : 链接另一个Index对象,产生一个新的Index
diff : 计算差集,并得到一个Index
intersection : 计算交集
union : 计算并集
isin : 计算一个指标各值是否都包含在参数集合中的布尔型数组
delete : 删除索引i出的元素,得到新的Index
drop : 删除传入的值,并得到新的Index
insert : 将元素插入到索引i出,并得到新的Index
is_momotonic : 当各元素均大于等于前一个元素时,返回True
is_unique : 当Index没有重复值时,返回True
unique : 计算Index中唯一值的数组
"""