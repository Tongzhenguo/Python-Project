# coding=utf-8
"""
http://blog.jasonding.top/2015/04/23/Machine%20Learning%20Experiments/【机器学习实验】使用朴素贝叶斯进行文本的分类
"""


from sklearn.datasets import fetch_20newsgroups
news = fetch_20newsgroups(subset='all')
print news.keys()
print type(news.data), type(news.target), type(news.target_names)
print news.target_names
print len(news.data)
print len(news.target)

news_train = fetch_20newsgroups(subset='train')
news_test = fetch_20newsgroups(subset='test')
X_train = news_train.data
X_test = news_test.data
Y_train = news_train.target
Y_test = news_test.target

##文本可以用词语的出现频率表征，这样可以完全忽略词在文本中的相对位置信息，这一点应该就保证了贝叶斯的条件独立性。
##由于我们使用词的出现次数作为特征，可以用多项分布来描述这一特征
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer
# nbc means naive bayes classifier
nbc_1 = Pipeline([
    ('vect', CountVectorizer()),
    ('clf', MultinomialNB()),
])
nbc_2 = Pipeline([
    ('vect', HashingVectorizer(non_negative=True)),
    ('clf', MultinomialNB()),
])
nbc_3 = Pipeline([
    ('vect', TfidfVectorizer()),
    ('clf', MultinomialNB()),
])
nbcs = [nbc_1, nbc_2, nbc_3]


#交叉验证
from sklearn.cross_validation import cross_val_score, KFold
from scipy.stats import sem
import numpy as np
def evaluate_cross_validation(clf, X, y, K):
    # create a k-fold croos validation iterator of k=5 folds
    cv = KFold(len(y), K, shuffle=True, random_state=0)
    # by default the score used is the one returned by score method of the estimator (accuracy)
    scores = cross_val_score(clf, X, y, cv=cv)
    print scores
    print ("Mean score: {0:.3f} (+/-{1:.3f})").format(
        np.mean(scores), sem(scores))
#将训练数据分成5份，输出验证的分数：
for nbc in nbcs:
    evaluate_cross_validation(nbc, X_train, Y_train, 5)


#优化提取单词规则参数
nbc_4 = Pipeline([
    ('vect', TfidfVectorizer(
                token_pattern=ur"\b[a-z0-9_\-\.]+[a-z][a-z0-9_\-\.]+\b",
    )),
    ('clf', MultinomialNB()),
])
evaluate_cross_validation(nbc_4, X_train, Y_train, 5)
#增加停词表
def get_stop_words():
    result = set()
    for line in open('learntoscikit/NB/stopwords_en.txt', 'r').readlines():
        result.add(line.strip())
    return result
stop_words = get_stop_words()
nbc_5 = Pipeline([
    ('vect', TfidfVectorizer(
                stop_words=stop_words,
                token_pattern=ur"\b[a-z0-9_\-\.]+[a-z][a-z0-9_\-\.]+\b",
    )),
    ('clf', MultinomialNB()),
])
evaluate_cross_validation(nbc_5, X_train, Y_train, 5)
#MultinomialNB有一个alpha参数，该参数是一个平滑参数，默认是1.0，我们将其设为0.01。
nbc_6 = Pipeline([
    ('vect', TfidfVectorizer(
                stop_words=stop_words,
                token_pattern=ur"\b[a-z0-9_\-\.]+[a-z][a-z0-9_\-\.]+\b",
    )),
    ('clf', MultinomialNB(alpha=0.01)),
])
evaluate_cross_validation(nbc_6, X_train, Y_train, 5)


# 评估分类器性能
from sklearn import metrics
nbc_6.fit(X_train, Y_train)
print "Accuracy on training set:"
print nbc_6.score(X_train, Y_train)
print "Accuracy on testing set:"
print nbc_6.score(X_test,Y_test)
y_predict = nbc_6.predict(X_test)
print "Classification Report:"
print metrics.classification_report(Y_test,y_predict)
print "Confusion Matrix:"
print metrics.confusion_matrix(Y_test,y_predict)
