import xgboost as xgb
import gzip
import numpy as np
import dataminingcontest.kaggle.Walmart_TripType_Classification.utils as utils

train,valid = utils.train_valid_split("../data_processing/train.csv")
train_ddmat, train_visitnum, train_tt = utils.make_ddcomb(train)
valid_ddmat, valid_visitnum, valid_tt = utils.make_ddcomb(valid)

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

xgb_params = {'max_depth': 12,
              'objective': 'reg:linear',
              'eval_metric': 'logloss',
              #          'num_class': 1,
              'subsample': 0.4,
              'colsample_bytree': 0.8,
              'eta': 0.01}

watchlist = [(dtrain, 'train'), (dtest, 'eval')]
bsta = xgb.train(xgb_params, dtrain, 5000, evals=watchlist, verbose_eval=True, early_stopping_rounds=500)