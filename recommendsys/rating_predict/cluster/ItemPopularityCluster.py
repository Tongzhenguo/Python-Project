# coding=utf-8
## 根据物品流行度分类
from recommendsys.rating_predict.basic.basic import basic
from recommendsys.rating_predict.basic.record import record
from recommendsys.rating_predict.cluster.Cluster import Cluster


class ItemPopularityCluster(Cluster):
    def __init__(self, records):
        """初始化分类方法，将结果存储到分组字典
        :param records:
        """
        Cluster.__init__(self, records)
        popularity = dict()
        b = basic()
        for r in records:
            if (r.test != 0):
                continue
            basic.AddToDict(b, popularity, r.item, 1)
        k = 0
        for item, n in sorted(popularity.items(), key=lambda p: p[1], reverse=False):
            c = int(5 * k / (1.0 * len(popularity)))
            self.group[item] = c
            k += 1

    def GetGroup(self, item):
        """
        :param item:
        :return:
        """
        if (item not in self.group):
            return -1
        else:
            return self.group[item]


# test
records = []
f_train = open("F:\code\Python-Project\dataset\guess your love\\train.csv")
for line in f_train.readlines():
    ss = line.strip("\n").split(",")
    records.append(record(user=ss[0], item=ss[1], score=ss[2], test=0))
f_test = open("F:\code\Python-Project\dataset\guess your love\\test.csv")
for line in f_test.readlines():
    ss = line.strip().split(",")
    records.append(record(user=ss[0], item=ss[1], score=0, test=1))

item_popularity_cluster = ItemPopularityCluster(records)
print item_popularity_cluster.group.values()
