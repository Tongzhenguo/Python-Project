# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from gensim import corpora, models, similarities
from pprint import pprint
import time

# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def load_stopword():
    f_stop = open('24.stopword.txt')
    sw = [line.strip() for line in f_stop]
    f_stop.close()
    return sw


if __name__ == '__main__':
    print '初始化停止词列表 --'
    t_start = time.time()
    stop_words = load_stopword()

    print '开始读入语料数据 -- '
    f = open('24.news.dat')    #24.LDA_test.txt
    texts = [[word for word in line.strip().lower().split() if word not in stop_words] for line in f]
    # texts = [line.strip().split() for line in f]
    print '读入语料数据完成，用时%.3f秒' % (time.time() - t_start)
    f.close()
    M = len(texts)
    print '文本数目：%d个' % M
    # pprint(texts)

    print '正在建立词典 --'
    dictionary = corpora.Dictionary(texts)
    V = len(dictionary)
    print u'词的个数：', V
    print '正在计算文本向量 --'
    corpus = [dictionary.doc2bow(text) for text in texts]
    print '正在计算文档TF-IDF --'
    t_start = time.time()
    corpus_tfidf = models.TfidfModel(corpus)[corpus]
    print '建立文档TF-IDF完成，用时%.3f秒' % (time.time() - t_start)
    print 'LDA模型拟合推断 --'
    num_topics = 10
    t_start = time.time()
    lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dictionary,
                            alpha=0.01, eta=0.01, minimum_probability=0.001,
                            update_every = 1, chunksize = 100, passes = 1)
    print 'LDA模型完成，训练时间为\t%.3f秒' % (time.time() - t_start)
    # # 所有文档的主题
    # doc_topic = [a for a in lda[corpus_tfidf]]
    # print 'Document-Topic:\n'
    # pprint(doc_topic)

    # 随机打印某10个文档的主题
    num_show_topic = 10  # 每个文档显示前几个主题
    print '10个文档的主题分布：'
    doc_topics = lda.get_document_topics(corpus_tfidf)  # 所有文档的主题分布
    idx = np.arange(M)
    np.random.shuffle(idx)
    idx = idx[:10]
    for i in idx:
        topic = np.array(doc_topics[i])
        print 'topic = \t', topic
        topic_distribute = np.array(topic[:, 1])
        # print topic_distribute
        topic_idx = topic_distribute.argsort()[:-num_show_topic-1:-1]
        print ('第%d个文档的前%d个主题：' % (i, num_show_topic)), topic_idx
        print topic_distribute[topic_idx]
    num_show_term = 7   # 每个主题显示几个词
    print '每个主题的词分布：'
    for topic_id in range(num_topics):
        print '主题#%d：\t' % topic_id
        term_distribute_all = lda.get_topic_terms(topicid=topic_id)
        term_distribute = term_distribute_all[:num_show_term]
        term_distribute = np.array(term_distribute)
        term_id = term_distribute[:, 0].astype(np.int)
        print '词：\t',
        for t in term_id:
            print dictionary.id2token[t],
        print
        # print '\n概率：\t', term_distribute[:, 1]
