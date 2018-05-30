# coding=utf-8
"""通用函数:快速的元素级数组函数

"""
import numpy as np

"abs fabs : 计算整数浮点数或复数的绝对值"
arr1 = np.array([1, -1, 2, -2])
print(np.abs(arr1))

"sqrt : 计算各元素平方根"
arr2 = np.arange(10)
print(np.sqrt(arr2))

"square : 计算个元素平方"
arr3 = np.arange(10)
print(np.square(arr3))

"exp : 计算个元素的指数"

"log、log10、1og2、"

"sign : 计算个元素的正负号: 1(正数) 0(零) -1(负数)"

"ceil : 大于等于该值的最小整数"
arr = np.array([1.2, 2.3, 3.4, 4.5, 5.6])
print(np.ceil(arr))

"floor : 小于等于该值的最大整数"

"rint : 将各元素值四舍五入为整数,保留dtype"

"modf : 将数组的小数和整数部分以两个独立数组的形式返回"

"isnan : 返回一个表示'哪些值不是数字'的布尔型数组"

"isfinite  isinf  :  表示有穷 无穷"

"cos、cosh、sin、sinh、tan、tanh  :  三角函数"
"arccos、arccosh、arcsin、arcsinh、arctan、arvtanh  :  反三角函数"

"""二元ufunc
"""

"add : 数组中对应元素相加"

"subtract : 第一个数组减去第二个数组"

"multiply : 数组元素相乘"

"divide、floor_divide : 除法或向下圆整除"

"power : 对应元素A的对应元素B次方"

"maximum、fmax : 计算最大值, 后者忽略NaN"
"minimum、fmin : 计算最小值, 后者忽略NaN"

"mod : 元素级的求模计算"

"copysign : 将第二个数组的值的符号赋值给第一个数组中的值"

"greater、greater_equal、less、less_equal、equal、not_equal : 元素级的比较运算 "

"logical_and、logical_or、logical_xor : 逻辑运算"