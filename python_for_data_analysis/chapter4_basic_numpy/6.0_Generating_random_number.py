# coding=utf-8
"""随机数生成

"""
import numpy as np
"部分numpy.random函数"
"seed : 确定随机数生成器的种子"

"permutation : 返回一个序列的随机排列或返回一个随机排列的范围"

"shuffle : 对一个序列就地随机排列"

"rand : 产生均匀分布的样本值"

"randint : 从给定的上下限范围内随机的选取整数"

"randn : 产生正态分布(平均值为0,标准差为1)的样本值"

"binomial : 产生二项分布的样本值"

"normal : 产生正态分布(高斯)的样本值"
samples = np.random.normal(size=(4, 4))
print(samples)
"beta : 产生beta 分布的样本值"