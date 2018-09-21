from sklearn.feature_extraction import DictVectorizer



"""

将映射列表转换为Numpy数组或scipy.sparse矩阵  

sklearn.feature_extraction.DictVectorizer(sparse = True)
sparse 是否转换为scipy.sparse矩阵表示，默认开启

方法
fit_transform(X,y)

应用并转化映射列表X，y为目标类型

inverse_transform(X[, dict_type])

将Numpy数组或scipy.sparse矩阵转换为映射列表

toarray() 和  sparse=False  使用一个就好
"""

onehot = DictVectorizer()

instances = [{'city': '北京', 'temperature': 100}, { 'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}]

X = onehot.fit_transform(instances).toarray()

# print(onehot.inverse_transform(X))

# print(X)

# 查看特征名字
# print(onehot.get_feature_names())



"""
文本特征抽取


"""

from sklearn.feature_extraction.text import CountVectorizer

content = ["life is short,i like python","life is too long,i dislike python"]

vectorizer = CountVectorizer()

# print(vectorizer.fit_transform(content).toarray())

# print(vectorizer.get_feature_names())


"""
tf*idf 词的重要性
"""

from sklearn.feature_extraction.text import TfidfVectorizer

content = ["life is short,i like python", "life is too long,i dislike python"]

vectorizer = TfidfVectorizer(stop_words='english')

print(vectorizer.fit_transform(content).toarray())

print(vectorizer.vocabulary_)

print(vectorizer.get_feature_names())