# coding=utf-8
"""DataFrame
DataFrame是表格型数据结构
含有一组有序的列,
既有行索引也有列索引
数据是以一个or多个二维块存放
"""
import pandas as pd
import numpy as np

"构建DataFrame"
data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = pd.DataFrame(data)
print(frame)
"可以用columns指定排列顺序"
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

"可以把DataFrame转变为Series"
print(frame['state'])
print(frame.year)

"列可以通过赋值的方式进行修改"
frame['state'] = np.arange(5)
print(frame)

"del 用于删除列"

"可以嵌套字典"
"外层字典的键作为列索引, 内层键作为行索引"
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
print(frame3)

"可以输入给DataFrame 的数据:"

"二维ndarray : 数据矩阵,还可以传入行标和列标"

"由数组列表或元组组成的字典 : 每个序列会变成DATaFrame的一列,序列长度必须相同"

"numpy的结构化/记录数组 : 类似于 '由数组组成的字典' "

"由Series 组成的字典 : 每个Series会成为一列,如果没有显式指定索引,则自动合成"

"由字典组成的字典 : 各内层字典会成为一列, 键会被合并成结果的行索引,"

"字典或Series 的列表 : 各项会成为DATa Frame的一行, 字典键或Series索引的并集成为DataFrame的列标"

"由列表或元组组成的列表 : 类似于'二维ndarray'"



"可以设置DataFrame的index和columns的name属性"
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)

"values 会返回二维ndarray形式的数据"
print(frame3.values)