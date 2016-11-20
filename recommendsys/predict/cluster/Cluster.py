# coding=utf-8
## 定义分类基类


class Cluster:
    def __init__(self, records):
        """构造函数
        :param records:
        """
        self.group = dict()

    def GetGroup(self, i):
        """默认是同一分类
        :param i:
        :return:
        """
        return 0
