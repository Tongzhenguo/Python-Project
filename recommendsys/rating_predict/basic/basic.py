# coding=utf-8
class basic:
    def AddToDict(self, mydict, key, value):
        """封装字典插入方法
        :param mydict:
        :param key:
        :param value:
        :return:
        """
        if (mydict.has_key(key)):
            mydict.setdefault(key, value)
        mydict[key] = value
