# -*- coding: utf-8 -*-

# @Time    : 2018/10/8 10:57
# @Author  : jin
# @File    : BGD.py

import numpy as np
import matplotlib as mpl
from sklearn.linear_model import LinearRegression
# 设置字符集防止中文乱码
mpl.rcParams["font.sans-serif"] = [u"simHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 创建数据
np.random.seed(0)
np.set_printoptions(linewidth=1000, suppress=True)

N = 10
x = np.linspace(0, 6, N) + np.random.randn(N)
y = 1.8 * x ** 3 + x ** 2 - 14 * x - 7 + np.random.randn(N)
x.shape = -1, 1
y.shape = -1, 1
# print(x)
# print(y)

# 在样本基础上进行模型的训练 （最小二乘法、 梯度下降）
lr = LinearRegression(fit_intercept=True)
lr.fit(x, y)
print("θ", lr.coef_)
print("截距", lr.intercept_)
print("R**2", lr.score(x, y))

