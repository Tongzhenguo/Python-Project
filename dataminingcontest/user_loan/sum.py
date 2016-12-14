# coding=utf-8
__author__ = 'arachis'

import pandas as pd

bank_detail_train_path = "E:/data/bank_detail_train.csv"
bank_detail_test_path = "E:/data/bank_detail_test.csv"
bill_detail_train_path = "E:/data/bill_detail_train.csv"
bill_detail_test_path = "E:/data/bill_detail_test.csv"
browse_test_path = "E:/data/browse_history_test.csv"
browse_train_path = "E:/data/browse_history_train.csv"


bank_sum_path = "E:/data/bank_sum.csv"
browse_sum_path = "E:/data/browse_sum.csv"
bill_sum_path = "E:/data/bill_sum.csv"



#特征的命名：在原始特征加前缀sum_
bank_detail_train = pd.read_csv(bank_detail_train_path) #6070197
bank_detail_test = pd.read_csv(bank_detail_test_path)
bank_detail = pd.concat([bank_detail_train, bank_detail_test])
# 收入，支出总额
bank_detail_n = (bank_detail.loc[:, ['uid', 'deal_type', 'deal_amount']]).groupby(['uid', 'deal_type']).sum()
bank_detail_n = bank_detail_n.unstack()
bank_detail_n.columns = ['sum_income', 'sum_outcome']
bank_detail_n.to_csv(bank_sum_path)


browse_train = pd.read_csv(browse_train_path,dtype="int64")
browse_test = pd.read_csv(browse_test_path,dtype="int64")
browse= pd.concat([browse_train, browse_test])
browse_n = browse[["uid","view_type","count"]].groupby(["uid", "view_type"]).sum()
browse_n = browse_n.unstack()
browse_n.columns = ["sum_x1","sum_x2","sum_x3","sum_x4","sum_x5","sum_x6","sum_x7","sum_x8","sum_x9","sum_x10","sum_x11"]
##缺失值0填充
browse_n = browse_n.fillna(0)
browse_n.to_csv(browse_sum_path)



bill_train = pd.read_csv(bill_detail_train_path)
bill_test = pd.read_csv(bill_detail_test_path)
bill = pd.concat([bill_train, bill_test])
bill.drop(["bill_time", "status","bid"], axis=1,inplace=True)
columns = [u'lastbill', u'last_repay', u'credit', u'bill_balance', u'min_repay',
       u'pay_count', u'bill', u'adjust', u'interest', u'available_balance',
       u'loan']
bill_n = bill.groupby(["uid"]).sum()
rename_dict = {s:'sum_'+s[:] for s in columns}
browse_n.rename(columns=rename_dict)
bill_n.to_csv(bill_sum_path)



