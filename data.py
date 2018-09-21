import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.umath_tests import inner1d

data_train = pd.read_csv("data/train.csv", encoding='utf-8')

data_train['Cabin'] = data_train['Cabin'].fillna('U')

ta = data_train.head(5)[['Age', 'Cabin']]
# print(ta)

# 采用出现最频繁的值填充
# freq_port = data_train.Age.dropna().mode()[0]
# data_train['Embarked'] = data_train['Embarked'].fillna(freq_port)
# print(freq_port)


# 采用中位数或者平均数填充
# data_train['Fare'].fillna(data_train['Fare'].dropna().median(), inplace=True)

# test_df['Fare'].fillna(test_df['Fare'].dropna().mean(), inplace=True)




# td = ta[ta.Age.notnull()].as_matrix()

# print(data_train["Sex"].isnull())

# print(data_train.dropna())

# 查看信息
# print(data_train.info())

# 查看统计信息
# print(data_train.describe())

# 画图

# fig = plt.figure()
# fig.set(alpha=0.2)  # 设定图表颜色alpha参数
#
# plt.subplot2grid((2,3),(0,0))             # 在一张大图里分列几个小图
# data_train.Survived.value_counts().plot(kind='bar')# 柱状图
# plt.title(u"获救情况 (1为获救)") # 标题
# plt.ylabel(u"人数")
#
# plt.subplot2grid((2,3),(0,1))
# data_train.Pclass.value_counts().plot(kind="bar")
# plt.ylabel(u"人数")
# plt.title(u"乘客等级分布")
#
# plt.subplot2grid((2,3),(0,2))
# plt.scatter(data_train.Survived, data_train.Age)
# plt.ylabel(u"年龄")                         # 设定纵坐标名称
# plt.grid(b=True, which='major', axis='y')
# plt.title(u"按年龄看获救分布 (1为获救)")
#
#
# plt.subplot2grid((2,3),(1,0), colspan=2)
# data_train.Age[data_train.Pclass == 1].plot(kind='kde')
# data_train.Age[data_train.Pclass == 2].plot(kind='kde')
# data_train.Age[data_train.Pclass == 3].plot(kind='kde')
# plt.xlabel(u"年龄")# plots an axis lable
# plt.ylabel(u"密度")
# plt.title(u"各等级的乘客年龄分布")
# plt.legend((u'头等舱', u'2等舱',u'3等舱'),loc='best') # sets our legend for our graph.
#
#
# plt.subplot2grid((2,3),(1,2))
# data_train.Embarked.value_counts().plot(kind='bar')
# plt.title(u"各登船口岸上船人数")
# plt.ylabel(u"人数")
# plt.show()


"""--------------缺省值处理------------------"""

from sklearn.ensemble import RandomForestRegressor


### 使用 RandomForestClassifier 填补缺失的年龄属性

def set_missing_ages(df):
    # 把已有的数值型特征取出来丢进Random Forest Regressor中

    age_df = df[['Age', 'Fare', 'Parch', 'SibSp', 'Pclass']]

    # 乘客分成已知年龄和未知年龄两部分
    known_age = age_df[age_df.Age.notnull()].as_matrix()
    unknown_age = age_df[age_df.Age.isnull()].as_matrix()

    # y即目标年龄
    y = known_age[:, 0]

    # X即特征属性值
    X = known_age[:, 1:]

    # fit到RandomForestRegressor之中
    rfr = RandomForestRegressor(random_state=0, n_estimators=2000, n_jobs=-1)

    rfr.fit(X, y)

    # 用得到的模型进行未知年龄结果预测
    predictedAges = rfr.predict(unknown_age[:, 1::])

    # 用得到的预测结果填补原缺失数据
    df.loc[(df.Age.isnull()), 'Age'] = predictedAges

    return df, rfr


def set_Cabin_type(df):
    df.loc[(df.Cabin.notnull()), 'Cabin'] = "Yes"
    df.loc[(df.Cabin.isnull()), 'Cabin'] = "No"
    return df

# data_train, rfr = set_missing_ages(data_train)
# data_train = set_Cabin_type(data_train)
