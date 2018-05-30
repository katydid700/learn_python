# coding=utf-8
"""用于布尔型数组的方法
sum可以用来计算布尔型数组的True值
"""
import numpy as np

arr = np.random.randn(100)
print((arr > 0).sum())

"any : 测试数组中是否有一个或以上的True"
"all : 是否所有都是True"
bools = np.array([False, False, True, False])

if bools.any():
    print("it's more at least one 'True'")
else:
    print("there is no 'True'")

"此外, 非0元素也会被当作True"