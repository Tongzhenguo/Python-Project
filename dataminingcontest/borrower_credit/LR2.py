# coding=utf-8
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
"""
优点：实现简单，易于理解和实现；计算代价不高，速度很快，存储资源低；
缺点：容易欠拟合，分类精度可能不高
注意：LR和GBRT最后都会转化为最优化问题，使用GD/GB方法求解，故都要进行归一化，以加速收敛和提高精度
参见：http://www.cnblogs.com/LBSer/p/4440590.html
是否特征选择：个人觉得只要过滤出相关性极低的特征即可，还在参考https://www.zhihu.com/question/28641663?sort=created
"""

#load data
train_x_csv = pd.read_csv("dataset\\borrower_credit\\train_x.csv")
train_y_csv = pd.read_csv("dataset\\borrower_credit\\train_y.csv")
test_csv = pd.read_csv("dataset\\borrower_credit\\test_x.csv")
test_x = test_csv.drop(test_csv.columns[[0]],axis=1).values

y_0 = train_y_csv[train_y_csv.y == 0]
merge = pd.merge(train_x_csv, y_0, how="inner", left_on=train_x_csv.uid,
                     right_on=y_0.uid)
X_ = train_x_csv.drop(train_x_csv.columns[[0]],axis=1) #index' axis = 0
for i in range(13458 / 1542 ):
    train_y_csv = train_y_csv.append(y_0)
    X_ = X_.append(merge.drop(merge.columns[[0,-2, -1]], axis=1))

#scale
scaler = preprocessing.StandardScaler()
X = scaler.fit(X_.values).transform(X_.values)
y = train_y_csv["y"].values
test_x = scaler.fit(test_x).transform(test_x)


#model select
n_features = X.shape[1]
C = 1.0
# #Create different classifiers.
# classifiers = {'L1 logistic': LogisticRegression(C=C, penalty='l1'),
#                'L2 logistic (OvR)': LogisticRegression(C=C, penalty='l2')
#                }
#
# n_classifiers = len(classifiers)
# import numpy as np
# for index, (name, classifier) in enumerate(classifiers.items()):
#     classifier.fit(X, y)
#     y_pred = classifier.predict(X)
#     classif_rate = np.mean(y_pred.ravel() == y.ravel()) * 100
#     print("classif_rate for %s : %f " % (name, classif_rate))

best_clf = LogisticRegression(C=C, penalty='l2')
best_clf.fit(X, y)
probas = best_clf.predict_proba(test_x)
pd.DataFrame(probas[:,1],index=test_csv.uid,columns=["score"]).\
    to_csv("dataset\\borrower_credit\LR2predict.csv")