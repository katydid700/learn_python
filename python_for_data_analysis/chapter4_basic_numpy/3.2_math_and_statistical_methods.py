# coding=utf-8
"""数学和统计方法
通过数组上的一组数学函数对整个数组或者某个轴向的数据进行统计计算
"""
import  numpy as np

arr =np.random.randn(5, 4)
"mean : 算术平均数"
print(arr.mean())
print(np.mean(arr))

"sum : 对数组的全部或某轴向的元素求和"
print(arr.sum())

print(arr.mean(axis=1))
print(arr.sum(0))

"std、var : 标准差和方差"

"min、max : 最大值和最小值"

"argmax、argmin : 最大值和最小值的索引"

"cumsum : 所有元素的累计和"
arr1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(arr1.cumsum(0))

"cumprod : 所有元素的累计积"
print(arr1.cumprod(1))