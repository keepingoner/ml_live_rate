# -*- coding: utf-8 -*-

# @Time    : 2018/9/28 11:53
# @Author  : jin
# @File    : 日期处理.py
import pandas as pd
import numpy as np
import datetime
import time

now = datetime.datetime.now()
# print(now)

# 时间差
new_date = now - datetime.datetime(2027, 9, 10, 10, 10, 16)
# print(new_date)

# 使用pandas
# dates = [['20170620'],
#          ['20170621'],
#          ['20170622'],
#          ['20170623'],
#          ['20170624']]
#
# data = pd.DatetimeIndex(dates)
# print(data)
# print(type(data))
# data = time.strftime("".join(data), "%Y-%m-%d")
# print(data)