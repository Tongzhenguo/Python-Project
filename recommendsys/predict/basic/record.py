# coding=utf-8
## 定义记录类


class record:
    def __init__(self, user, item, score=0, test=0, predict=0):
        """
        :param user:
        :param item:
        :param score:
        :param test:
        :param predict:
        """
        self.user = user
        self.item = item
        self.score = score
        self.test = test
        self.predict = predict
