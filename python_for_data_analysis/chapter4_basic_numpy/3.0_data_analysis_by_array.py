# coding=utf-8
"""例用数组进行数据处理
用数组表达式代替循环的做法,被称为矢量化

"""
import numpy as np
import matplotlib.pyplot as plt
"meshgrid : 接受两个一维数组,返回两个二维矩阵"
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs)
print(ys)
z = np.sqrt(xs ** 2 + ys ** 2)
plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()
