# coding=utf-8
"""
    翻译自：http://pandas.pydata.org/pandas-docs/stable/10min.html
    http://pandas.pydata.org/pandas-docs/stable/merging.html
"""

import numpy as np
import pandas as pd

### 一、创建对象
## 1.可以传递一个list对象创建一个Series,Pandas会默认创建整型索引
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print s

## 2.通过传递一个numpy array,时间索引以及列标签来创建一个DataFrame
# dates = pd.date_range('20130101', periods=6)
# print dates
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# print df
## 3.通过传递一个能够被转换成类似序列结构的字典对象来创建一个DataFrame
# df2 = pd.DataFrame({"A": 1, "B": pd.Timestamp('20130102'), "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#                     "D": np.array([3] * 4, dtype="int32"), "E": pd.Categorical(["test", "train", "test", "train"]),
#                     "F": "foo"})
# print df2

### 二、查看数据
## 1.查看frame中头部和尾部的行,默认5行
# print df.head()
# print df.tail(3)

## 2.显示索引，列和底层的numpy数据
# print df.index
# print df.columns
# print df.values

## 3.describe()函数对于数据的款素统计汇总,python中方法不能省略圆括号
# print df.describe()

## 4.对数据的转置
# print df.T

## 5.按轴（列）进行排序
# print df.sort_index(axis=1,ascending=False)

## 6.按值进行排序,建议使用sort_values(by=)
# print df.sort(columns="B")
# print df.sort_values(by="B")

### 三、选择
##  推荐使用优化方法： .at, .iat, .loc, .iloc and .ix.
## 获取1.选择一个单独的列,这将会返回一个Series,等同于df.A
# print df["A"]

## 获取2.通过[]进行选择，这将会对行进行切片
# print df[0:3][1:2]
# print df[0:3]

##上面的方法是通过下标[]进行访问，下面可以.loc[]来对指定便签进行选择
##通过标签选择：1.使用便签来获取一个交叉的区域
# print df.loc[ dates[0] ]

##通过标签选择：2.通过标签来在多个轴上进行选择
# print df.loc[ :,["A","B"] ]

##通过标签选择：3.标签切片
# print df.loc[ "20130102":"20130104",["A","B"] ]

##通过标签选择：4.对于返回的对象进行维度缩减
# print df.loc["20130102",["A","B"]]

##通过标签选择：5.获取一个标量
# print df.loc[ dates[0],"A" ]

##通过标签选择：6.快速访问一个标量(at方法)
# print df.at[ dates[0],"A" ]

##通过位置选择：1.通过传递数值进行位置选择（选择的是行）
# print df.iloc[3]

##通过位置选择：2.通过数值进切片
# print df.iloc[3:5,0:2]

##通过位置选择：3.通过指定一个位置的列表
# print df.iloc[ [1,2,3],[0,2] ]

##通过位置选择：4.对行进行切片
# print df.iloc[1:3,:]

##通过位置选择：5.对列进行切片
# print df.iloc[:,1:3]

##通过位置选择:6.获取特定的值
# print df.iloc[1,1]
# print df.iat[1,1]

##可以使用逻辑表达式来选择指定的数据框
##布尔索引：1.使用一个单独列的值来选择数据
# print df[df.A > 0]

##布尔索引：2.使用where操作来选择数据
# print df[ df > 0]

##布尔索引：3.使用isin()方法来过滤
# print df2[df2["E"].isin( ["test"] )]

##设置：通过一个numpy数组设置一组新值
# df.loc[ :,"E" ] = np.array( [5]*len(df) )
# print df

## reindex对索引进行改变/新增/删除(未赋值就是pd.nan)
# df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])
# print df1

### 四、缺失值处理（pandas使用np.nan代替缺失值，默认不会计算）
## 1.去掉包含缺失值的行
## 1.去掉包含缺失值的行
# print df1.dropna(how="any")

## 2.对缺失值进行填充
# print df1.fillna(value=5)

## 3.判断缺失值
# print  pd.isnull()

## 五、相关操作
##apply(对数据应用函数）
# print df.apply(np.cumsum)##累积和
# print df.apply(lambda x:x.max - x.min) ##x代表当前列的一个标量

##值计数器
# print s.value_counts()

##六、聚合（aggregate）
## 1.contat(拼接,默认是全外联)
# piece = [ df[:2],df[2:4],df[4:] ]
# print pd.concat(piece)  ##默认axis=0是上下连接
# piece = [ df.loc[ :,["A","B"] ],df.loc[ :,["C","D"] ] ]
# print pd.concat(piece,axis=1) ##1是左右连接
#更高级拼接操作：http://pandas.pydata.org/pandas-docs/stable/merging.html
# result = pd.concat([df1, df4], axis=1, join='inner')

## 2.联表操作（join,merge）
# left = pd.DataFrame( {
#     "key":["foo","foo1"],"lval":[1,2]
# } )
# right = pd.DataFrame( {
#     "key":["foo","foo2"],"rval":[1,2]
# } )
# print pd.merge(left,right,how="inner",left_on=left.key,right_on=right.key) ##内联
# print pd.merge(left,right,how="left",left_on=left.key,right_on=right.key)  ##左联
# print pd.merge(left,right,how="right",left_on=left.key,right_on=right.key) ##右联
# print pd.merge(left,right,how="outer",left_on=left.key,right_on=right.key)  ##全外联
# print left.set_index("key").join([right.set_index("key")], how="outer")  ##join根据索引连接
# print "多列名做为内链接的连接键\r\n",merge(data,data2,on=("name","id"))

## 3.append(追加)
# print df.append(other=[df,df]) ##只能上下联接

## 4.分组
# print df.groupby("A").sum()
# print df.groupbyoupby( ["A","B"] ).sum()  ##层次索引
# print df.groupby(['A', 'B'])['C'].mean()
# print df.groupby(df["A"])

### 七、Reshaping
# 1.Stack
# tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
#                      'foo', 'foo', 'qux', 'qux'],
#                     ['one', 'two', 'one', 'two',
#                     'one', 'two', 'one', 'two']]))
# index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
# df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# df2 = df[:4]
# print df2
# # The stack function “compresses” a level in the DataFrame’s columns to produce either:
# # A Series, in the case of a simple column Index
# # A DataFrame, in the case of a MultiIndex in the columns
# stacked = df2.stack()
# print stacked
# print stacked.unstack()
# print stacked.unstack(1)
# print stacked.unstack(0)

## 2.数据透视表
# print pd.pivot_table(df,values="D",index=["A","B"],columns="C")

### 八、时间序列
rng = pd.date_range("1/1/2012", periods=100, freq="S")
ts = pd.Series(np.random.randn(0, 500, len(rng)), index=rng)
print ts.resample("5Min",how="sum")

### 九、Categorical类型
## http://pandas.pydata.org/pandas-docs/stable/categorical.html#categorical
### 十、画图
## http://pandas.pydata.org/pandas-docs/stable/visualization.html#visualization

### 十一、导入和保存数据
df.to_csv("data.csv")
csv = df.read_csv("data.csv")
