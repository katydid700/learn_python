# coding=utf-8
"""范例: 随机漫步

"""
import random
import numpy as np
import matplotlib.pyplot as plt

position = 0
walk = [position]
steps = 1000
for i in xrange(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

