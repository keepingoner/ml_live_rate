# -*- coding: utf-8 -*-

# @Time    : 2018/9/21 13:54
# @Author  : jin
# @File    : 预处理离散化.py

###离散化与面元划分
import numpy as np
import pandas as pd

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(' cats =  ', cats)

#
# '''
# [(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (25, 35], (60, 100], (35, 60], (35, 60], (25, 35]]
# Length: 12
# Categories (4, object): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]
# '''
#
print(' cats.labels =  ', cats.labels)  # [0 0 0 1 0 0 2 1 3 2 2 1]
#
# print(' cats.levels =  ', cats.levels)  # Index(['(18, 25]', '(25, 35]', '(35, 60]', '(60, 100]'], dtype='object')
#
# print(pd.value_counts(cats))  # 计数
# '''
# (18, 25]     5
# (35, 60]     3
# (25, 35]     3
# (60, 100]    1
# dtype: int64
# '''
#
# cats_2 = pd.cut(ages, [18, 26, 36, 61, 100], right=False)
# print(cats_2)
# '''
# [(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ...
# , (25, 35], (60, 100], (35, 60], (35, 60], (25, 35]]
# '''
#
# group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
# group_names_ = pd.cut(ages, bins, labels=group_names)
# print(' group_names_ = ', group_names_)
# '''
# [Youth, Youth, Youth, YoungAdult, Youth, ..., YoungAdult, Senior, MiddleAged, MiddleAged, YoungAdult]
# Length: 12
# '''
#
# data = np.random.rand(20)
# pd.cut(data, 4, precision=2)
#
# data = np.random.randn(1000)  # Normally distributed 正态分布 / 常态分布
# cats = pd.qcut(data, 4)  # Cut into quartiles
# cats
#
# pd.value_counts(cats)
#
# pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])
