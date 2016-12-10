import pandas as pd

bank_detail_train_path = "E:/data/bank_detail_train.csv"
bank_detail_test_path = "E:/data/bank_detail_test.csv"
bill_detail_train_path = "E:/data/bill_detail_train.csv"
bill_detail_test_path = "E:/data/bill_detail_test.csv"
browse_test_path = "E:/data/browse_history_test.csv"
browse_train_path = "E:/data/browse_history_train.csv"

bank_detail_train = pd.read_csv(bank_detail_train_path) #6070197
bank_detail_train[bank_detail_train.timestamp == 0].shape[0] #38773
bank_detail_train.groupby(by=["uid","timestamp"],axis=1)

bank_detail_test = pd.read_csv(bank_detail_test_path) #376409
bank_detail_test[bank_detail_test.timestamp == 0].shape[0] #3138



bill = pd.read_csv(bill_detail_train_path)
bill[bill.bill_time == 0].shape[0] #427447
merge = pd.merge(bank_detail_train,bill,on=["uid"])



