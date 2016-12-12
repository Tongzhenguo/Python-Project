#coding=utf-8


import matplotlib.pylab as plt
import pandas as pd

merge_null_path = "E:/data/merge_null.csv"
overdue_train = "E:/data/overdue_train.csv"

train = pd.read_csv(merge_null_path)[['uid','n_null']]
train_y = pd.read_csv(overdue_train,dtype='int64')
train = pd.merge(train,train_y,on='uid')
train = train.sort(columns='n_null')


t = train.n_null.values
y = train.overdue.values
y0 = [ i+1-sum(y[0:i+1]) for i in range(len(y))]
x = range(len(t))
plt.scatter(x,t,c='k')
plt.plot(x,y0,c='b')
plt.title('train set')
plt.show()

##空值不是特别多


