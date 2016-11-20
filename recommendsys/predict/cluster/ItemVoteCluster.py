# coding=utf-8
### 根据用户评分的平均值分类
from recommendsys.predict.basic.basic import basic
from recommendsys.predict.cluster.Cluster import Cluster


class ItemVoteCluster(Cluster):
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
            basic.AddToDict(b, vote, r.item, r.score)
            basic.AddToDict(b, count, r.item, 1)
        k = 0
        for item, v in vote.items():
            ave = int(v) / (count[item] * 1.0)
            c = int(ave * 2)
            self.group[item] = c

    def GetGroup(self, item):
        """
        :param uid:
        :return:
        """
        if (item not in self.group):
            return -1
        else:
            return self.group[item]

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
            # cluster = ItemVoteCluster(records)
            # print cluster.group.keys()
