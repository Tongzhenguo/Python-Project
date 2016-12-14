import pandas as pd
from sklearn import preprocessing

browse_mean = "E:/data/browse_mean.csv"
bill_mean = "E:/data/bill_mean.csv"

browse = pd.read_csv(browse_mean).drop(["uid"],axis=1)
scaler = preprocessing.StandardScaler().fit(browse.values)
print  sorted(scaler.scale_,reverse=True)


bill = pd.read_csv(bill_mean).drop(["uid"],axis=1)
scaler = scaler.fit(bill.drop(["status"],axis=1).values)
print sorted(scaler.scale_,reverse=True)


