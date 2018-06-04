# coding=utf-8
"""手工处理分隔符格式

"""
import numpy as np
import pandas as pd
import csv
f = open('ch06/ex7.csv')
reader = csv.reader(f)
"对reader进行迭代将会为每行产生一个列表"
for line in reader:
    print(line)
"为了使格式合乎要求,需要对其他做一些整理工作"
lines = list(csv.reader(open('ch06/ex7.csv')))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)

"CSV语支选项"
"""
delimiter : 用于分隔符的单字符字符串,默认为','
lineterminator : 用于写操作的行结束符,默认为'\r\n' 
quotechar : 用于带有特殊字符的字段的引用符号
quotin : 引用约定,
skipinitialspace : 忽略分隔符后面的空白符,默认为False
doublequoter : 如何处理字段内的引用符号。如果为True,则双写
ecapechar : 用于对分隔符进行转义的字符串
"""