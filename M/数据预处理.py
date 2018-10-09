
"""特征处理 通过特定的统计方法或者数学方法，将数据转化为算法要求的数据
标准缩放；
1 /归一化
2/ 标准化

"""

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# 使用较少，因为出现异常数据影响最大最小值
def min_max():
    """

    :return:
    """

    mm = MinMaxScaler(feature_range=(2, 3))

    data = mm.fit_transform([[96, 68, 50, 20], [98, 79, 31, 54]])

    print(data)


# 标准化使用较多
def stand_vec():
    """

    :return:
    """
    std = StandardScaler()

    data = std.fit_transform([[96, 68, 50, 20], [98, 79, 31, 54]])

    print(data)


if __name__ == "__main__":

    # min_max()

    stand_vec()