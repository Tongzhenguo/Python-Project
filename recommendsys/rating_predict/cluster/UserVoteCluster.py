# coding=utf-8
### 根据用户评分的平均值分类
from recommendsys.rating_predict.basic.basic import basic
from recommendsys.rating_predict.cluster.Cluster import Cluster


class UserVoteCluster(Cluster):
    def __init__(self, records):
        """初始化分类，将结果存在group字典
        :param records:
        """
        Cluster.__init__(self, records)
        vote = dict()
        count = dict()
        b = basic()
        for r in records:
            if (r.test != 0):
                continue
            basic.AddToDict(b, vote, r.user, r.score)
            basic.AddToDict(b, count, r.user, 1)
        k = 0
        for user, v in vote.items():
            ave = int(v) / (count[user] * 1.0)
            c = int(ave * 2)
            self.group[user] = c

    def GetGroup(self, uid):
        """
        :param uid:
        :return:
        """
        if (uid not in self.group):
            return -1
        else:
            return self.group[uid]

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
            #
            # cluster = UserVoteCluster(records)
            # print cluster.group.keys()
