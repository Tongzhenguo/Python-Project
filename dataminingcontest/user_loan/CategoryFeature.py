# coding=utf-8
import pandas as pd
from sklearn import preprocessing

#将用户信息类别类型进行独热编码
user_info_train = pd.read_csv("E:/data/user_info_train.csv")
uidList = user_info_train["uid"].tolist() #55596
X = user_info_train.drop(["uid"], axis=1).values
enc = preprocessing.OneHotEncoder()
enc.fit(X)
enc_Feature = enc.transform(X).toarray()
pd.DataFrame(enc_Feature,index=uidList).to_csv("E:/data/userInfoTrain_Category.csv")


user_info_test = pd.read_csv("E:/data/user_info_test.csv")
uidList = user_info_test["uid"].tolist() #55596
X = user_info_test.drop(["uid"], axis=1).values
enc = preprocessing.OneHotEncoder()
enc.fit(X)
enc_Feature = enc.transform(X).toarray()
pd.DataFrame(enc_Feature,index=uidList).to_csv("E:/data/userInfoTest_Category.csv")



