"""
介绍数据预处理


二、标准化(Standardization)，或者去除均值和方差进行缩放
公式为：(X-X_mean)/X_std 计算时对每个属性/每列分别进行.

将数据按其属性(按列进行)减去其均值，然后除以其方差。最后得到的结果是，对每个属性/每列来说所有数据都聚集在0附近，方差值为1。


sklearn.preprocessing.scale(X, axis=0, with_mean=True,with_std=True,copy=True)

根据参数的不同，可以沿任意轴标准化数据集。

参数解释：

X：数组或者矩阵
axis：int类型，初始值为0，axis用来计算均值 means 和标准方差 standard deviations. 如果是0，则单独的标准化每个特征（列），如果是1，则标准化每个观测样本（行）。
with_mean: boolean类型，默认为True，表示将数据均值规范到0
with_std: boolean类型，默认为True，表示将数据方差规范到1

X.mean(axis=0)用来计算数据X每个特征的均值；

X.std(axis=0)用来计算数据X每个特征的方差；

preprocessing.scale(X)直接标准化数据X。

"""

from sklearn import preprocessing
import numpy as np

X_train = np.array([[1., -1., 2.], [2., 0., 0.], [0., 1., -1.]])

X_scaled = preprocessing.scale(X_train)

# print(X_scaled)

X_mean = X_train.mean(axis=0)

X_std = X_train.std(axis=0)

X1 = (X_train - X_mean) / X_std

# print(X1)


# 方法2：sklearn.preprocessing.StandardScaler类


scaler = preprocessing.StandardScaler()

X_scaled2 = scaler.fit_transform(X_train)

# print(X_scaled2)

# X1 和X_trrain X_trrain2的值是相同的

"""

三、将特征的取值缩小到一个范围（如0到1）
除了上述介绍的方法之外，另一种常用的方法是将属性缩放到一个指定的最大值和最小值(通常是1-0)之间，这可以通过preprocessing.MinMaxScaler类来实现。

使用这种方法的目的包括：

1、对于方差非常小的属性可以增强其稳定性；
2、维持稀疏矩阵中为0的条目。
下面将数据缩至0-1之间，采用MinMaxScaler函数

"""
min_max_scaler = preprocessing.MinMaxScaler()

X_train_minmax = min_max_scaler.fit_transform(X_train)

# print(X_train_minmax)
#
# print(min_max_scaler.scale_)
#
# print(min_max_scaler.min_)

"""
注意：这些变换都是对列进行处理。

当然，在构造类对象的时候也可以直接指定最大最小值的范围：feature_range=(min, max)，此时应用的公式变为：

"""

X_std = (X_train - X_train.min(axis=0)) / (X_train.max(axis=0) - X_train.min(axis=0))

X_minmax = X_std / (X_train.max(axis=0) - X_train.min(axis=0)) + X_train.min(axis=0)

"""
四、正则化(Normalization)
正则化的过程是将每个样本缩放到单位范数(每个样本的范数为1)，如果要使用如二次型(点积)或者其它核方法计算两个样本之间的相似性这个方法会很有用。

该方法是文本分类和聚类分析中经常使用的向量空间模型（Vector Space Model)的基础.

Normalization主要思想是对每个样本计算其p-范数，然后对该样本中每个元素除以该范数，这样处理的结果是使得每个处理后样本的p-范数(l1-norm,l2-norm)等于1。

"""
# 方法1：使用sklearn.preprocessing.normalize()函数

X_normalized = preprocessing.normalize(X_train, norm='l2')

# print(X_normalized)

# 方法2：sklearn.preprocessing.StandardScaler类
normalizer = preprocessing.Normalizer().fit(X_train)
# 然后使用正则化实例来转换样本向量：

# print(normalizer.transform(X_train))

# 两种方法都可以，效果是一样的。


"""
五、二值化(Binarization)

特征的二值化主要是为了将数据特征转变成boolean变量。在sklearn中，sklearn.preprocessing.Binarizer函数可以实现这一功能。实例如下：

"""

binarizer = preprocessing.Binarizer().fit(X_train)

# 带参数 Binarizer(threshold=1.1)   threshold为阀值 结果数据值大于阈值的为1，小于阈值的为0


binarizer.transform(X_train)

# print(binarizer.transform(X_train))


"""
六、缺失值处理
由于不同的原因，许多现实中的数据集都包含有缺失值，要么是空白的，要么使用NaNs或者其它的符号替代。
这些数据无法直接使用scikit-learn分类器直接训练，所以需要进行处理。
幸运地是，sklearn中的Imputer类提供了一些基本的方法来处理缺失值，如使用均值、中位值或者缺失值所在列中频繁出现的值来替换。


"""

from sklearn.preprocessing import Imputer

X = [[1, 2], [np.nan, 3], [7, 6]]

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)

data = imp.fit_transform(X)

print(data)

X = [[np.nan, 2], [6, np.nan], [7, 6]]

print(imp.transform(X))
