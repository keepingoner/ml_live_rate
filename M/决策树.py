
"""
def __init__(self,
                 criterion="gini",   基尼系数
                 splitter="best",
                 max_depth=None,  树的深度大小

                 min_samples_split=2, # 减枝
                 min_samples_leaf=1,  # 减枝

                 min_weight_fraction_leaf=0.,
                 max_features=None,
                 random_state=None,  随机数种子
                 max_leaf_nodes=None,
                 min_impurity_decrease=0.,
                 min_impurity_split=None,
                 class_weight=None,
                 presort=False):
"""

from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

# 获取数据
data = pd.read_csv("data/train.csv")

x = data[["Pclass", "Age", "Sex"]]

y = data["Survived"]

# 缺失值处理
x["Age"].fillna(x["Age"].mean(), inplace=True)

# 分为训练 测试

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

# 特征工程 将sex 转换为onehot编码
dict = DictVectorizer(sparse=False)



x_train = dict.fit_transform(x_train.to_dict(orient='record'))

x_test = dict.transform(x_test.to_dict(orient='record'))

# print(dict.feature_names_)

# 使用决策树
dec = DecisionTreeClassifier()

dec.fit(x_train, y_train)

print("预测准确率", dec.score(x_test, y_test))


dt_predict = dec.predict(x_test)

# print("预测结果", dt_predict)

print(classification_report(y_test, dt_predict, target_names=["died", "survived"]))


# 数的结构显示

# 导出图像显示
# exp = export_graphviz(dec, out_file="./tree.dot", feature_names=['年龄', 'Pclass', 'Sex=female', 'Sex=male'])

# 使用随机森林


rfc = RandomForestClassifier()

rfc.fit(x_train, y_train)

rfc_y_predict = rfc.predict(x_test)

print(rfc.score(x_test, y_test))

print(classification_report(y_test, rfc_y_predict, target_names=["died", "survived"]))
