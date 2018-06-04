# coding=utf-8
"""二进制数据格式

"""
import numpy as np
import pandas as pd

frame = pd.read_csv('ch06/ex1.csv')
frame.save('ch06/frame_pickle')
"AttributeError: 'DataFrame' object has no attribute 'save'"