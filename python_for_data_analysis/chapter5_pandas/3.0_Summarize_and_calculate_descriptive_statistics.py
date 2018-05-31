# coding=utf-8
"""汇总和计算描述统计

"""
import numpy as np
import pandas as pd

df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
                   [np.nan, np.nan], [0.75, -1.3]],
                  index=['a', 'b', 'c', 'd'],
                  columns=['one', 'two'])
print(df)
"sum 会返回一个含有列小计的Series"
print(df.sum())
"传入axis=1将会按行进行求和运算"
print(df.sum(axis=1))

"约简方法的选项"
"""
axis : 约简的轴。DataFrame的行用0,列用1
skipna : 排除缺失值,默认值为True
level : 如果轴是层次化索引(MultiIndex),则根据level分组约简
"""

"描述和汇总统计"

"""
count : 非NA值的数量
describe : 针对Series 或 各DataFrame列计算汇总统计
min、max : 计算最小值和最大值
argmin、argmax : 计算能够获取最小值和最大值的索引位置
idxmin : 返回最小值的索引
idxmax : 返回最大值的索引
quantile : 计算样本的分位数
sum : 值的总和
mean : 值的平均数
median : 值的算术中位数
mad : 根据平均值计算平均绝对离差
var : 样本值的方差
std : 样本值的标准差
skew : 样本值的偏度
kurt : 样本值的峰度
cumsum : 样本值的累计和
cummin、cummax : 样本值的累计最小值和累计最大值
cumprod : 样本值的累计值
diff : 计算一阶差分
pct_change : 计算百分数变化
"""
print(df.idxmax())
