# -*- coding: utf-8 -*-
import numpy as np

"""
创建数组
"""
a = np.arry([1,2,3,4])
b = np.arry([5,6,7,8])
c = np.arry([[1,2,3,4],
             [4,5,6,7],
             [7,8,9,10]])
"""
显示数组的形状
"""
a.shape
b.shape
c.shape
"""
改变形状 
如果为-1 则自动计算长度
"""
c.shape = 4,3
c.shape = 2,-1
"""
reshape 构建制定形状的新数组
"""
d = a.reshape
