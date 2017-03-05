# coding=utf-8
import nltk

#浏览可用软件包
# nltk.download()

from nltk.book import *
from nltk.misc import babelize_shell

print text1

#搜索文本
text1.concordance('monstrous')

#查看还有哪些词出现在相似的上下文中
text1.similar('monstrous')
print
text2.similar('monstrous')

#查看共同上下文
print text2.common_contexts(['monstrous','very'])

#频数分布
fdist = FreqDist(text1)
print fdist
print fdist.keys()[:50]
fdist.plot(50,cumulative=True)

#找指定频率和长度的词
fdist5 = FreqDist(text5)
print sorted( [w for w in set(text5) if len(w)>7 and fdist5[w]>7 ] )

#词语搭配和双联词（2-grams）
# nltk.bigrams(['more','is',''])

#高于单词频的双联词
text4.collocations()

#机器翻译
babelize_shell()
#the pig that John found looked happy
#german

#对话系统
nltk.chat

#