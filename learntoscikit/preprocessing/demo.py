# coding=utf-8
from learntoscikit.LRforFeatureSelect import iris
from sklearn import preprocessing
from numpy import vstack, array, nan
from sklearn.preprocessing import Imputer

__author__ = 'arachis'

"""
    缺失值处理（填充负值，填充中值，填充众数，剔除，单独作为一个特征）
"""

##直接使用pandas 中的异常值处理
import pandas as pd
import numpy as np
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
# df1.fillna(-1)  ##填充负值
df1.dropna() ## 剔除

#缺失值计算，返回值为计算缺失值后的数据
#参数missing_value为缺失值的表示形式，默认为NaN
#参数strategy为缺失值填充方式，默认为mean（均值）
# strategy : string, optional (default="mean")
#         The imputation strategy.
#
#         - If "mean", then replace missing values using the mean along
#           the axis.
#         - If "median", then replace missing values using the median along
#           the axis.
#         - If "most_frequent", then replace missing using the most frequent
#           value along the axis.
print Imputer().fit_transform( vstack((array([nan, nan, nan, nan]), iris.data)) )

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
print enc.fit([[0,0],[0,1],[1, 0], [2,1]]) #all leaf
print enc.transform([[1, 0], [2,1]]).toarray() #小男孩，小女孩


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
poly = PolynomialFeatures(2)#自由度为2
print poly.fit_transform(X)

"""
    生成自定义特征转换（FunctionTransformer）
"""
from numpy import log1p
from sklearn.preprocessing import FunctionTransformer
#自定义转换函数为对数函数的数据变换
#第一个参数是单变元函数
print( FunctionTransformer(log1p).fit_transform(iris.data) )


"""
    滤除方差小的数据(Removing features with low variance)
"""
from sklearn.feature_selection import VarianceThreshold
sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
print sel.fit_transform(X)

"""
    相关性分析（皮尔逊相关系数）
"""
from sklearn.feature_selection import SelectKBest
from scipy.stats import pearsonr

#选择K个最好的特征，返回选择特征后的数据
#第一个参数为计算评估特征是否好的函数，该函数输入特征矩阵和目标向量，输出二元组（评分，P值）的数组，
#数组第i项为第i个特征的评分和P值。在此定义为计算相关系数
#参数k为选择的特征个数
def calc(X,Y):
    ls = []
    for x in X.T:
        ls.append( pearsonr(x, Y) )
    return array(ls)
print SelectKBest(calc, k=2).fit_transform(iris.data, iris.target)

"""
    相关性分析（互信息法）
"""
# from sklearn.feature_selection import SelectKBest
# #由于MINE的设计不是函数式的，定义mic方法将其为函数式的，返回一个二元组，二元组的第2项设置成固定的P值0.5
# def calc_entropy(x, y):
#     pass
# #选择K个最好的特征，返回特征选择后的数据
# print SelectKBest(calc_entropy, k=2).fit_transform(iris.data, iris.target)

