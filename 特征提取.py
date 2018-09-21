from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba

# 数据抽取和分类


def dict_vec():
    """
    字典数据抽取
    :return:
    """
    a = [{"city": "beijing", "tmp": 100}, {"city": "shanghai", "tmp": 60}, {"city": "neimeng", "tmp": 10}]

    ab_dic = DictVectorizer(sparse=False)

    data = ab_dic.fit_transform(a)

    # 特征值的抽取
    print(ab_dic.get_feature_names())

    print(data)


def con_vec():
    """
    文本抽取
    :return:
    """
    a = ["i like python", 'python is short']

    ab_dic = CountVectorizer()

    data = ab_dic.fit_transform(a)

    # 特征值的抽取
    print(ab_dic.get_feature_names())

    # 使用toarray方法
    print(data.toarray())


def cut_word():

    con1 = jieba.cut("我喜欢中国，我爱中国")
    con2 = jieba.cut("我喜欢python，我爱python")

    print(con1, con2)

    content1 = list(con1)
    content2 = list(con2)

    print(content1, content2)

    c1 = " ".join(content1)
    c2 = " ".join(content2)
    return c1, c2


def han_con_vec():
    """
    汉字提取
    :return:
    """

    c1, c2 = cut_word()

    ab_dic = CountVectorizer()

    data = ab_dic.fit_transform([c1, c2])

    # 特征值的抽取
    # print(ab_dic.get_feature_names())

    # 使用toarray方法
    # print(data.toarray())


def tfidf_con_vec():
    """
    tf * idf 重要性
    :return:
    """

    c1, c2 = cut_word()

    ab_dic = TfidfVectorizer()

    data = ab_dic.fit_transform([c1, c2])

    # 特征值的抽取
    # print(ab_dic.get_feature_names())

    # 使用toarray方法
    print(data.toarray())


if __name__ == "__main__":

    dict_vec()
    #
    # # con_vec()
    #
    # # cut_word()
    #
    # # han_con_vec
    #
    # tfidf_con_vec()

