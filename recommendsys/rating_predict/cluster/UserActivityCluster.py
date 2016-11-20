# coding=utf-8
### 根据用户活跃对对用户分类
from recommendsys.rating_predict.basic.basic import basic
from recommendsys.rating_predict.cluster.Cluster import Cluster


class UserActivityCluster(Cluster):
    def __init__(self, records):
        """调用父类构造方法
        :param records:
        """
        Cluster.__init__(self, records)
        activity = dict()
        b = basic()
        for r in records:
            if (r.test != 0):
                continue
            basic.AddToDict(b, activity, r.user, 1)
        k = 0
        for user, n in sorted(activity.items(), key=lambda a: a[1], reverse=False):
            c = int((5 * k) / (1.0 * len(activity)))
            self.group[user] = c
            k += 1

    def GetGroup(self, uid):
        """通过内部的group字典，获取对应的用户流行度分组
        :param uid:
        :return:
        """
        if uid not in self.group:
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
            # cluster = UserActivityCluster(records)
            # print cluster.group.values()
