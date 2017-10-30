#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-22 下午3:24
# @Author  : huiqin
# @File    : pandass.py
# @Software: PyCharm Community Edition
# @Description : Class is for
import pandas as pd
import numpy as np
df = pd.DataFrame({'key1':['a','a','b','b'],
                   'key2':['one','two','one','two'],
                   'data1':np.random.randn(4),
                   'data2':np.random.randn(4)})
print(df)

# one
grouped = df['data1'].groupby(df['key1'])
print(grouped)
print(grouped.mean())

# two
print(df.groupby('key1').mean())
print(df.groupby(['key1','key2']).mean())
print(df.groupby('key1')['data1'])
# df.groupby('key1')['data1'] 与