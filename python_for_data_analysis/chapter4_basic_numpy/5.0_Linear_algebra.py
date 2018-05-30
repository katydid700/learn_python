# coding=utf-8
"""线性代数

"""
import numpy as np

"dot : 矩阵的乘法"
x = np.array([[1., 2., 3. ], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x.dot(y))
print(np.dot(x, y))

"常用的numpy.linalg函数"
"diag : 以一维数组的形式返回方阵的对角线元素, 或将一维数组转为方阵"

"dot : 矩阵的乘法"

"trace : 计算对角线的元素和"

"det : 计算矩阵的行列式"

"eig : 计算方阵的本征值和本征向量"

"inv : 计算方阵的逆"

"pinv : 计算矩阵的moore-penrose伪逆"

"qr : 计算QR分解"

"svd : 计算奇异值分解"

"solve : 解线性方程Ax = b, A为一个方阵"

"lstsq : 计算Ax = b 的最小二乘"