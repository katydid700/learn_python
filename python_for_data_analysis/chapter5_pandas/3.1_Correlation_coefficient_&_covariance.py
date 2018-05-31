# coding=utf-8
"""相关系数和协方差
有些汇总统计是通过'参数对'计算出来的
"""
import numpy as np
import pandas as pd
import pandas.io.data as web

all_data = {}
for ticker in ['AAPL', 'IBM', 'MSFT', 'GOOG']:
    all_data[ticker] = web.get_data_yahoo(ticker, '1/1/2000', '1/1/2010')

price = pd.DataFrame({tic: data['Adj Close']
                      for tic, data in all_data.iteritems()})
volume = pd.DataFrame({tic: data['Volume']
                      for tic, data in all_data.iteritems()})

returns = price.pct_change
print(returns.tail())

"The pandas.io.data module is moved to a separate package " \
"ImportError: The pandas.io.data module is moved to a separate package" \
"(pandas-datareader). After installing the pandas-datareader package" \
"(https://github.com/pydata/pandas-datareader), you can change the import " \
"``ffrom pandas.io import data, wb`` to ``from pandas_datareader import data, wb``"
