# coding=utf-8
"""Series
Series是一种类似于一维数组的对象,
由一组数据和一组相关的数据标签所组成
"""
import pandas as pd

obj = pd.Series([4, 7, -5, 3])
print(obj)

"values属性"
print(obj.values)

"index属性"
print(obj.index)

"自定义index"
obj2 = pd.Series([4, 7, -5, 3], index=['d', 'v', 'c', 'a'])
print(obj2)
print(obj2.index)

"可以通过索引选取一个或多个值"
print(obj2['d'])
print(obj2[['d', 'v']])

"数组运算会保留索引和值之间的链接"
print(obj2[obj2 > 0])

"可以直接用dict数据创建Series"
sdata = {'aaa':100, 'bbb':200, "ccc":300, "ddd":400}
obj3 = pd.Series(sdata)
print("obj3:")
print(obj3)
states = {'aaa', 'vvv', 'bbb', 'ccc', 'ddd'}
obj4 = pd.Series(sdata, index=states)
print(obj4)
"isnull notnull 用来检查缺失数据"
print(obj4.isnull())
print(pd.isnull(obj4))

"算术运算中索引会自动匹配"
print(obj3 + obj4)

"Series对象本身和索引都有一个name属性"
obj4.name = 'alhpabet'
print(obj4)

"索引可以通过赋值的方式修改"
obj4.index = ['x', 'xx', 'xxx', 'xxxx', 'xxxxx']
print(obj4)
"看来不支持可变操作,如下:"
obj4.index[0] = ['a']
print(obj4)