# coding=utf-8
"""
获取文本语料库和词汇资源
"""
from nltk.corpus import gutenberg

print gutenberg.fileids()
#文本统计
for fileid in gutenberg.fileids():
    num_char = len( gutenberg.raw(fileid) ) #原始内容
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len( set([w.lower for w in  gutenberg.words(fileid)]) )
print int(num_char),int(num_words),int(num_sents),int(num_vocab)

#网络和聊天语料库
from nltk.corpus import webtext
for fileid in webtext.fileids():
    print fileid,
