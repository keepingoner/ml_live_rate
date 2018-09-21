# -*- coding: utf-8 -*-

# @Time    : 2018/9/20 14:53
# @Author  : jin
# @File    : one.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

datasets = pd.read_csv("datasets/studentscores.csv")
X = datasets.iloc[:, : 1].values
Y = datasets.iloc[:, 1].values

X_train, X_test, Y_train, Y_test = train_test_split( X, Y, test_size = 1/4, random_state = 0)

regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)

# sco = regressor.score(X_train, Y_train)
# print(sco)
# # Training results
# plt.scatter(X_train , Y_train, color = 'y')
# plt.plot(X_train , regressor.predict(X_train), color ='blue')
#
# # test results
# # plt.scatter(X_test , Y_test, color = 'r')
# # plt.plot(X_test , regressor.predict(X_test), color ='c')
#
# plt.show()
# print(predict)

# #散点图
# plt.figure(figsize=(6, 6))
# size = 50
# colour = "r"
# plt.scatter(X, Y, s=size, c=colour)
# # 横纵坐标
# plt.xlabel("hour")
# plt.ylabel("scores")
# # 标题
# plt.title("时间分数关系")
# 中文乱码问题
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# plt.show()
