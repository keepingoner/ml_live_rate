# -*- coding: utf-8 -*-

# @Time    : 2018/9/28 16:01
# @Author  : jin
# @File    : 模型保存和持久.py

from sklearn.externals import joblib

joblib.dump("模型名字", "路径")

joblib.load("路径")

