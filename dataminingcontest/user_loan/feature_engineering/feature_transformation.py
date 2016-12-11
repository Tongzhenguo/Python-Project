import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder

browse_mean = "E:/data/browse_mean.csv"
bill_mean = "E:/data/bill_mean.csv"
overdue_train = "E:/data/overdue_train.csv"
uid_test = "E:/data/usersID_test.csv"


np.random.seed(10)

bill = pd.read_csv(bill_mean)
overdue = pd.read_csv(overdue_train,dtype='int64')
test = pd.read_csv(uid_test)

data = pd.merge(overdue, bill, on=["uid"]).drop(["uid"],axis=1).values
merge = pd.merge(test, bill, how="left",on=["uid"]).drop(["uid"],axis=1).fillna(0)
X, y = data[:,:13],overdue.overdue.values[:53174]
X_test = merge.values


grd = GradientBoostingClassifier(learning_rate=0.01,n_estimators=1000)
grd_enc = OneHotEncoder()
grd_lm = LogisticRegression()
grd.fit(X, y)
grd_enc.fit(grd.apply(X)[:, :, 0])

# ## bill transform to tree leaf encode
# leaf_code_feature = grd_enc.transform(grd.apply(bill.drop(["uid"],axis=1))[:, :, 0]).toarray()
# tree_feature_bill = pd.DataFrame(data=leaf_code_feature, index=bill.uid)
# tree_feature_bill.to_csv("E:/data/tree_feature_bill.csv")


## predict
grd_lm.fit(grd_enc.transform(grd.apply(X)[:, :, 0]), y)
y_pred_grd_lm = grd_lm.predict_proba(grd_enc.transform(grd.apply(X_test)[:, :, 0]))
pd.DataFrame(index=test.uid,data=y_pred_grd_lm[:,1],columns=["proba"]).to_csv("E:/data/grd_lm_predict.csv")