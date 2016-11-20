# coding=utf-8
## 均方根误差
import math


def RMSE(records):
    return math.sqrt(sum([(int(r.score) - r.predict) ** 2 for r in records]) / float(len(records)))

# test
# records = []
# f_train = open("F:\code\Python-Project\dataset\guess your love\\train.csv")
# for line in f_train.readlines():
#     ss = line.strip("\n").split(",")
#     records.append(record(user=ss[0], item=ss[1], score=ss[2],test=0))
# f_test = open("F:\code\Python-Project\dataset\guess your love\\test.csv")
# for line in f_test.readlines():
#     ss = line.strip().split(",")
#     records.append(record(user=ss[0], item=ss[1], score=0,test=1))

# mean.predictAll(records,UserActivityCluster(records),ItemPopularityCluster(records))
# print RMSE(records)
# mean.predictAll(records,UserVoteCluster(records),ItemVoteCluster(records))
# print RMSE(records)
# mean.predictAll(records,UserActivityCluster(records),ItemVoteCluster(records))
# print RMSE(records)
# mean.predictAll(records,UserVoteCluster(records),ItemPopularityCluster(records))
# print RMSE(records)
