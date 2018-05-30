# coding=utf-8
"""将数组以二进制形式保存到磁盘


"""
import numpy as np

arr = np.arange(10)

np.save('some_array', arr)
f = np.load('some_array.npy')
print(f)

"savez : 可以将多个数组保存到一个压缩文件中"
"加载时会得到类似字典的对象"

np.savez('array_archive.npz', a=arr, b=arr)
arch = np.load('array_archive.npz')
print(arch['b'])