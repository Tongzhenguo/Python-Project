# coding=utf-8
__author__ = 'arachis'
import pandas as pd

bank_mean_path = "E:/data/bank_mean.csv"
bill_mean_path = "E:/data/bill_mean.csv"
browse_mean_path = "E:/data/browse_mean.csv"

merge_path = "E:/data/merge.csv"

# merge
bank_mean = pd.read_csv(bank_mean_path)
bill_mean = pd.read_csv(bill_mean_path)
browse_mean = pd.read_csv(browse_mean_path)

data = pd.merge(bank_mean,browse_mean,how="outer",on=["uid"]).merge(bill_mean,how="outer",on=["uid"]).fillna(0)
# data.describe()  #发现有很多空值

data.to_csv(merge_path)



