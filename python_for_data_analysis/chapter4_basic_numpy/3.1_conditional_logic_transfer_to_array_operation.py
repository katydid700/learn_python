# coding=utf-8
"""将条件逻辑表述为数组运算

"""
import numpy as np

"numpy.where : 三元表达式x if condition else y 的矢量化版本"

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = np.where(cond, xarr, yarr)
print(result)

"将一个随机矩阵的正数替换为2,负数替换为-2"
arr = np.random.randn(4, 4)
print(np.where(arr > 0, 2, -2))
print(np.where(arr > 0, 2, arr))
