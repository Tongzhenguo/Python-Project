import xgboost as xgb
import numpy as np
import pandas as pd
import dataminingcontest.kaggle.Walmart_TripType_Classification.utils as utils
from dataminingcontest.kaggle.Walmart_TripType_Classification.data_processing import preproc

#data processing
trainfile = preproc("../walmart-input/train.csv")
test = preproc('../walmart-input/test.csv')

#split trainset and validset
train,valid = utils.train_valid_split(trainfile)

train_ddmat, train_visitnum, train_tt = utils.make_ddcomb(train,train)
valid_ddmat, valid_visitnum, valid_tt = utils.make_ddcomb(valid,train)

n = len(train_tt)
key = 31
ttt_key = np.zeros(n)
vtt_key = np.zeros(len(valid_tt))

for i in range(n):
    ttt_key[i] = 1 if (train_tt[i] == key) else 0

for i in range(len(valid_tt)):
    vtt_key[i] = 1 if (valid_tt[i] == key) else 0

dtrain = xgb.DMatrix(train_ddmat[0:n], label=ttt_key)
dtest = xgb.DMatrix(valid_ddmat, label=vtt_key)

xgb_params = {'max_depth': 8,
              'objective': 'multi:softprob',
              'eval_metric': 'mlogloss',
              'num_class': 39,
              'subsample': 0.4,
              'colsample_bytree': 0.8,
              'eta': 0.01}

watchlist = [(dtrain, 'train'), (dtest, 'eval')]
bsta = xgb.train(xgb_params, dtrain, 500, evals=watchlist, verbose_eval=True, early_stopping_rounds=500)
yhat = bsta.predict(dtest)
# print yhat[:5,]


# sub = pd.read_csv('../walmart-input/sample_submission.csv')
# print sub.values.shape
# print yhat.shape
# for i in range( len(sub["VisitNumber"].values) ):
#     sub[:,i+1] = yhat[:,i]
# print sub.head()