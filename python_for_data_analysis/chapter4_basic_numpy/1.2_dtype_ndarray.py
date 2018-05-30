# coding=utf-8

"""dtype

"""
import numpy as np
arr = np.array([1,2,3,4,5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)