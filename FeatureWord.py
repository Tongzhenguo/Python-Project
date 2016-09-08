# coding=utf-8
import jieba as jieba

__author__ = 'YYT'
def readEssay(self):
        """生成特征词集合"""
        one_block = ""
        f = "E:\doc\技术\R\脚本\\" + "倚天屠龙记" + ".txt"
        with open(f, "r") as my_file :
            line = my_file.read()
            print line
        word_list = list(jieba.cut(line, cut_all = False))
        word_dict = {}
        for word in word_list :
            if word not in word_dict :
                word_dict[word] = 1
            else :
                word_dict[word] += 1
        word_dict = sorted(word_dict.iteritems(), key = lambda d :d[1], reverse = True)
        self.feature = []
        for word, fre in word_dict :
            self.feature.append(word)
        self.feature = self.feature[ : self.dimension]
        for word in self.feature :
            print word,
readEssay
