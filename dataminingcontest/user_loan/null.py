import pandas as pd

bank_detail_train = pd.read_csv("E:/data/bank_detail_train.csv") #6070197
bank_detail_train[bank_detail_train.timestamp == 0].shape[0] #38773

bank_detail_test = pd.read_csv("E:/data/bank_detail_test.csv") #376409
bank_detail_test[bank_detail_test.timestamp == 0].shape[0] #3138



