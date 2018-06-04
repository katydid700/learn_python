# coding=utf-8
"""读写文本格式的数据
本书着重讲解 pandas 的输入输出对象
"""
import numpy as np
import pandas as pd

"表: pandas 中的解析函数"
"""
read_csv : 从文件、URL、文件型对象中加载带分隔符的数据。默认分隔符为逗号
read_table : 从文件、URL、文件型对象中加载带分隔符的数据。默认分隔符为制表符("\t")
read_fwf : 读取定宽列表格式数据(没有分隔符)
read_clipborad : 读取剪贴板中的数据
"""

"上述函数在将文本数据转换为DataFrame时所用到的一些技术"
"""
索引 : 将一个或多个列当作返回的DataFrame处理,以及是否从文件、用户获取列名
类型推断和数据转换 : 包括用户定义值的转换、缺失值标记列表等
日期解析 : 包括组合功能,比如将分散在多个列中日期时间信息组合成结果中的单个列
迭代 : 支持对大文件进行逐块迭代
不规整数据问题 : 跳过一些行、页脚、注释或其他一些不重要的东西
"""

df = pd.read_csv('ch06/ex1.csv')
print(df)

"分配默认的列名或者自定义列名"
print(pd.read_csv('ch06/ex2.csv', header=None))
names=['a', 'b', 'c', 'd', 'message']
print(pd.read_csv('ch06/ex2.csv', names=names))
"如果希望把message列做成DataFrame的索引,可以用index_col"
print(pd.read_csv('ch06/ex2.csv', names=names, index_col='message'))

"多个列做成一个层次化索引,传入由列编号或列名组成的列列表即可"
print(pd.read_csv('ch06/csv_mindex.csv', index_col=['key1', 'key2']))

"对于不是用固定的分隔符去分割字段的,可以编写一个正则表达式来作为read_table的分隔符"
print(pd.read_table('ch06/ex3.txt', sep='\s+'))

"对于缺失值,默认情况下,pandas会用一组经常出现的标记值进行识别"
print(pd.read_csv('ch06/ex5.csv'))

"表 : read_csv/read_table 函数的参数"
"""
path : 表示文件系统位置、URL、文件型对象的字符串
sep或delimiter : 用于对行中各字段进行拆分的字符号或正则表达式
header : 用作列名的行号,默认为0
index_col : 用作行索引的列编号或列名
names : 用于结果的列名列表
skiprows : 需要忽略的行数
na_values : 一组用于替换NA的值
comment : 用于将注释信息从行尾拆分出去的字符
parse_data : 尝试将数据解析为日期,默认为False
keep_data_col : 如果链接多列解析日期,则保持参与连接的列, 默认为False
converters : 由列号/列名跟函数之间的映射关系组成的字典。列如{'foo':f}会对foo列所有值应用函数f
dayfirst : 当解析有歧义的日期时,将其看作国际格式,默认为False
date_parser : 用于解析日期的函数
nrows : 需要读取的行数(从开始处算起)
iterator : 返回一个TextParser以便逐块读取文件
chunksize : 文件块的大小(用于迭代)
skip_footer :需要忽略的行数(从文件结尾处算起)
verbose : 打印各种解释器输出信息,如'非数值列中缺失值的数量'等
encoding : 用于Unicode的文本编码格式,如'utf-8'表示用UTF-8编码的文本
squeeze : 如果数据经解析后仅含一列,则返回Series
thousands : 千分位分隔符
"""