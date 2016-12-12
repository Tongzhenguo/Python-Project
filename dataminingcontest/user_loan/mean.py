# coding=utf-8
import pandas as pd

bank_detail_train_path = "E:/data/bank_detail_train.csv"
bank_detail_test_path = "E:/data/bank_detail_test.csv"
bill_detail_train_path = "E:/data/bill_detail_train.csv"
bill_detail_test_path = "E:/data/bill_detail_test.csv"
browse_test_path = "E:/data/browse_history_test.csv"
browse_train_path = "E:/data/browse_history_train.csv"


bank_mean_path = "E:/data/bank_mean.csv"
bill_mean_path = "E:/data/bill_mean.csv"
browse_mean_path = "E:/data/browse_mean.csv"


bank_detail_train = pd.read_csv(bank_detail_train_path) #6070197
# bank_detail_train[bank_detail_train.timestamp == 0].shape[0] #38773
bank_detail_test = pd.read_csv(bank_detail_test_path)
bank_detail = pd.concat([bank_detail_train, bank_detail_test])
# 在该数据集中，一个用户对应多条记录，这里我们采用对每个用户每种交易类型取均值进行聚合(参考DC源码分享)
bank_detail_n = (bank_detail.loc[:, ['uid', 'deal_type', 'deal_amount','timestamp']]).groupby(['uid', 'deal_type']).mean()
# 重塑数据集，并设置字段（列）名称
bank_detail_n = bank_detail_n.unstack()
bank_detail_n.columns = ['income', 'outcome', 'income_tm', 'outcome_tm']
bank_detail_n.to_csv(bank_mean_path)



bill_train = pd.read_csv(bill_detail_train_path)
bill_test = pd.read_csv(bill_detail_test_path)
bill = pd.concat([bill_train, bill_test])
bill_mean = bill.groupby(["uid"]).mean()
bill_mean.drop('bid',axis=1,inplace=True)

bill_mean.to_csv(bill_mean_path)


browse_train = pd.read_csv(browse_train_path)
browse_test = pd.read_csv(browse_test_path)
browse= pd.concat([browse_train, browse_test])
browse_n = browse[["uid","view_type","count"]].groupby(["uid", "view_type"]).mean()
browse_n = browse_n.unstack()
browse_n.columns = ["count1","count2","count3","count4","count5","count6","count7","count8","count9","count10","count11"]
##缺失值0填充
browse_n = browse_n.fillna(0)
browse_n.to_csv(browse_mean_path)