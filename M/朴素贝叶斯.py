"""
互联网新闻分类
"""
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


news = fetch_20newsgroups(subset="all")

X = news.data

Y = news.target

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

vec = CountVectorizer()

X_train = vec.fit_transform(X_train)

X_test = vec.transform(X_test)

mnb = MultinomialNB(alpha=1.0)

mnb.fit(X_train, Y_train)

y_predict = mnb.predict(X_test)

print(y_predict)

print(mnb.score(X_test, Y_test))





