# coding=utf-8
"""整数索引
整数索引可能有歧义
"""
import numpy as np
import pandas as pd

"为了保持良好的一致性,如果你的轴索引含有索引器" \
"那么根据整数进行数据选取的操作将总是面向标签的"