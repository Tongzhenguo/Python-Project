# coding=utf-8
__author__ = 'arachis'

import numpy as np
from sklearn import preprocessing

"""
    缺失值处理（填充负值，填充中值，填充众数，剔除，单独作为一个特征）
"""


"""
    异常值处理（剔除）
"""


"""
    z-score:均值为0，方差为1(标准化)(基于列向量)
"""
X_train = np.array([[ 1., -1.,  2.],\
           [ 2.,  0.,  0.],\
           [ 0.,  1., -1.]])
X_test = np.array([[ -3., -1.,  4.]])
X_scaled = preprocessing.scale(X_train)
print  X_scaled

#Scaled data has zero mean and unit variance:
print X_scaled.mean(axis=0)
print X_scaled.std(axis=0)

#Scaler
scaler = preprocessing.StandardScaler().fit(X_train)
print scaler.transform(X_train)
print scaler.transform(X_test)

print scaler.mean_
print scaler.scale_

"""
    min-max score：映射到区间[0,1]（最小-最大规范化）(基于列向量)
"""
scaler = preprocessing.MinMaxScaler()
print scaler.fit_transform(X_train)
print scaler.transform(X_test) #新的数据可能会不在[0,1]区间内


"""
    规范化（Normalization）（归一化）(基于行向量)
"""
normalizer = preprocessing.Normalizer(norm='l2')
print normalizer.fit_transform(X_train)
print normalizer.fit_transform(X_test)


"""
    二值化（Binarization）
"""
#给定阈值，将特征转换为0/1
binarizer = preprocessing.Binarizer(threshold=1.1)
print binarizer.transform(X_train)
print binarizer.transform(X_test)


"""
    类别特征编码（Encoding categorical features）
"""
#知道各个类别的数目，可通过n_values指定
enc = preprocessing.OneHotEncoder()
print enc.fit([[1, 2, 3], [0, 2, 0]])
print enc.transform([[1, 0, 0]]).toarray()


"""
    标签编码（Label encoding）
"""
#非数值型转化为数值型
le = preprocessing.LabelEncoder()
le.fit(["paris", "paris", "tokyo", "amsterdam"])
print le.transform(["tokyo", "tokyo", "paris"])


"""
    生成多项式特征（Generating polynomial features）
"""
# （x1,x2） => (1,x1,x2,x1^2,x1*x2,x2^2)
from sklearn.preprocessing import PolynomialFeatures
X = np.arange(6).reshape(3, 2)
poly = PolynomialFeatures(2)
print poly.fit_transform(X)



"""
    滤除方差小的数据(Removing features with low variance)
"""
from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
sel.fit_transform(X)