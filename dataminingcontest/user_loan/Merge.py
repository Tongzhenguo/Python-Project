# coding=utf-8
__author__ = 'arachis'
import pandas as pd

bank_mean_path = "E:/data/bank_mean.csv"
bill_mean_path = "E:/data/bill_mean.csv"
browse_mean_path = "E:/data/browse_mean.csv"

merge_path = "E:/data/merge.csv"
dataset_path = "E:/data/dataset.csv"


# merge
bank_mean = pd.read_csv(bank_mean_path)
bill_mean = pd.read_csv(bill_mean_path)
browse_mean = pd.read_csv(browse_mean_path)

data = pd.merge(bank_mean,browse_mean,how="outer",on=["uid"]).merge(bill_mean,how="outer",on=["uid"]).fillna(0)
# data.describe()  #发现有很多空值
data.to_csv(merge_path,index=None)

def merge3file(bank_file,bill_file,browse_file,merge_file):
       bank_mean = pd.read_csv(bank_file)
       bill_mean = pd.read_csv(bill_file)
       browse_mean = pd.read_csv(browse_file)
       data = pd.merge(bank_mean,browse_mean,how="outer",on=["uid"]).merge(bill_mean,how="outer",on=["uid"]).fillna(0)
       data.to_csv(merge_file,index=None)


def mergeDataset(dataset_file,new_file,merge_file):
       dataset = pd.read_csv(dataset_file)
       dataset_new = pd.read_csv(new_file)
       data = pd.merge(dataset, dataset_new, how="outer", on=["uid"]).fillna(0)
       data.to_csv(merge_file,index=None)

user_info_test_path = "E:/data/userInfoTest_Category.csv"
user_info_train_path = "E:/data/userInfoTrain_Category.csv"
user_info_path = "E:/data/userInfo_category.csv"
user_info_test = pd.read_csv(user_info_test_path,dtype='int64')
user_info_train = pd.read_csv(user_info_train_path,dtype='int64')
user_info = pd.concat([user_info_train, user_info_test])
user_info.columns = ["uid",  u'enc_1', u'enc_2', u'enc_3', u'enc_4', u'enc_5', u'enc_6', u'enc_7', u'enc_8',
       u'enc_9', u'enc_10', u'enc_11', u'enc_12', u'enc_13', u'enc_14', u'enc_15', u'enc_16', u'enc_17',
       u'enc_18',u'enc_19', u'enc_20', u'enc_21', u'enc_22', u'enc_23',u'enc_24']
user_info.to_csv(user_info_path,index=None)



loan_time_train_path = "E:/data/loan_time_train.csv"
loan_time_test_path = "E:/data/loan_time_test.csv"
loan_time_train = pd.read_csv(loan_time_train_path,dtype='int64')
loan_time_test = pd.read_csv(loan_time_test_path,dtype='int64')
loan_time = pd.concat([loan_time_train, loan_time_test])
loan_time.to_csv("E:/data/loan_time.csv",index=None)


##merge all to a bigtable
data = pd.merge(user_info, data, how="outer", on=["uid"]).merge(loan_time,how="outer", on=["uid"])
data.to_csv(dataset_path,index=None)


##merge all count to a bigtable
bank_sum_path = "E:/data/bank_sum.csv"
bill_sum_path = "E:/data/bill_sum.csv"
browse_sum_path = "E:/data/browse_sum.csv"
merge_count_path = "E:/data/merge_count.csv"

merge3file(bank_sum_path,bill_sum_path,browse_sum_path,merge_count_path)

mergeDataset(dataset_path,merge_count_path,"E:/data/merge_dataset.csv")



