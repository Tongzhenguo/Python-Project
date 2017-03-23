# !/usr/bin/python
# -*- coding:utf-8 -*-

import jieba.posseg


if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    f = open('.\\26.novel.txt')
    str = f.read().decode('utf-8')
    f.close()

    #this only works using dt, custom POSTokenizer instances are not supported.
    """
    dt = POSTokenizer(jieba.dt)，POSTokenizer就是jieba分词中的词性标注定义的类，其中jieba.dt是jieba自己实现的分词接口。
    POSTokenizer类在初始化的时候，会读取离线统计的词典（每行分别为字、频率、词性），加载为词--词性词典。
    """
    seg = jieba.posseg.cut(str)
    for s in seg:
        print s.word, s.flag, '|',
        # print s.word, '|',
