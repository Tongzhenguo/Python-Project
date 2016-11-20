# coding=utf-8
from recommendsys.rating_predict.cluster.Cluster import Cluster


class IdCluster(Cluster):
    def __init__(self, records):
        """调用父类的构造方法
        :param records:
        """
        Cluster.__init__(self, records)

        # def GetGroup(self,i):
