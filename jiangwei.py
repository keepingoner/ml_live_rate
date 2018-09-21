
"""
降维  降的是特征数量

1/特征选择
2/主成分分析 PCA

n_components 小数   90% -95% 最好 经验
n_components 整数 减少到的特征数量  一般不使用整数

特征选择三大武器  1 过滤 variance 方差为0  基本不变化 2 嵌入式 （正则、决策树） 3 包裹

"""

from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA

# 使用较少，因为出现异常数据影响最大最小值


def min_max():
    """
    删除低方差的特征
    :return:
    """

    mm = VarianceThreshold(threshold=0)

    data = mm.fit_transform([[96, 68, 50, 20], [98, 79, 31, 54]])

    print(data)


def main_sele():
    """
    主成分分析
    :return:
    """
    mm = PCA(n_components=0.9)

    data = mm.fit_transform([[96, 68, 50, 20], [98, 79, 31, 54]])

    print(data)


if __name__ == "__main__":

    # min_max()
    main_sele()
