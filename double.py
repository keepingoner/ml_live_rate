import pandas as pd
from sklearn.preprocessing import Imputer

data = pd.read_csv("data/11.csv")

x = data[0:2]
# []  逗号前是 行 逗号后是列

#
# print(x)
#
# imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
#
# imputer = imputer.fit(x)
#
# z = imputer.transform(x)
#
# print(z)
#
# # 用平均代替 缺失值
#
# from sklearn.preprocessing import LabelEncoder
#
# labelencoder = LabelEncoder()

