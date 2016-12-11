# coding=utf-8
import pandas as pd

browse_rank_path = "E:/data/browse_rank.csv"
bill_rank_path = "E:/data/bill_rank.csv"
bank_rank_path = "E:/data/bank_rank.csv"
browse_discretization_path = 'E:/data/browse_discretization.csv'
bill_discretization_path = 'E:/data/bill_discretization.csv'
bank_discretization_path = 'E:/data/bank_discretization.csv'


browse_rank = pd.read_csv(browse_rank_path)
browse_x = browse_rank.drop(["uid"], axis=1)
# 59327L / 10
browse_x[browse_x < 5932] = 1
browse_x[browse_x >= 5932*9] = 10
for i in range(2,10,1):
    browse_x[(browse_x >= 5932*(i-1)) &(browse_x < 5932*i)] = i
#离散特征命名：前缀d
rename_dict = {s:'d'+s[1:] for s in browse_x.columns.tolist()}
train_x = browse_x.rename(columns=rename_dict)
train_x['uid'] = browse_rank.uid
train_x.to_csv(browse_discretization_path, index=None)


bill = pd.read_csv(bill_rank_path)
bill_x = bill.drop(["uid"], axis=1)
# 66817L / 10
step = 66817L / 10
bill_x[bill_x < step] = 1
bill_x[bill_x >= step*9] = 10
for i in range(2,10,1):
    bill_x[(bill_x >= step*(i-1)) &(bill_x < step*i)] = i
rename_dict = {s:'d'+s[1:] for s in bill_x.columns.tolist()}
bill_x = bill_x.rename(columns=rename_dict)
bill_x['uid'] = bill.uid
bill_x.to_csv(bill_discretization_path, index=None)


bank = pd.read_csv(bank_rank_path)
bank_x = bank.drop(["uid"], axis=1)
step = 10003L / 10
bank_x[bank_x < step] = 1
bank_x[bank_x >= step*9] = 10
for i in range(2,10,1):
    bank_x[(bank_x >= step*(i-1)) &(bank_x < step*i)] = i
rename_dict = {s:'d'+s[1:] for s in bank_x.columns.tolist()}
bank_x = bank_x.rename(columns=rename_dict)
bank_x['uid'] = bank.uid
bank_x.to_csv(bank_discretization_path, index=None)