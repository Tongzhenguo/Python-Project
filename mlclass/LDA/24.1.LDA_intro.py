# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
LDA,LSI类API熟悉
LSI适合短文本
LDA适合长文本
"""

from gensim import corpora, models, similarities
from pprint import pprint

# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


if __name__ == '__main__':
    f = open('24.LDA_test.txt')
    stop_list = set('for a of the and to in'.split())
    # texts = [line.strip().split() for line in f]
    # pprint(texts)
    texts = [[word for word in line.strip().lower().split() if word not in stop_list] for line in f]
    # print 'Text = '
    # pprint(texts)

    dictionary = corpora.Dictionary(texts)#初始化词典，词汇编码到词的映射
    V = len(dictionary) #the bag-of-words format = list(（token_id, token_count）)
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpus_tfidf = models.TfidfModel(corpus)[corpus]
    # corpus_tfidf = corpus

    # print 'TF-IDF:'
    # for c in corpus_tfidf:
    #     print c

    print '\nLSI Model:'
    lsi = models.LsiModel(corpus_tfidf, num_topics=2, id2word=dictionary)
    topic_result = [a for a in lsi[corpus_tfidf]]#再用原始语料预测一遍
    # LSI在计算得到主题的同时，有时候会得到负数。我们虽然可以解释成“这个文档排斥该主题”或“这个主题排斥该词”，但总是觉得不合理。
    pprint(topic_result)

    # print 'LSI Topics:'
    # pprint(lsi.print_topics(num_topics=2, num_words=5))
    # similarity = similarities.MatrixSimilarity(lsi[corpus_tfidf])   # similarities.Similarity()
    # print 'Similarity:'
    # pprint(list(similarity))


    print '\nLDA Model:'
    num_topics = 2 #  `alpha` and `eta` are hyperparameters that affect sparsity of the document-topic
        #(theta) and topic-word (lambda) distributions.两个狄利克雷先验分布的参数
    lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dictionary,
                          alpha='auto', eta='auto', minimum_probability=0.001)
    doc_topic = [doc_t for doc_t in lda[corpus_tfidf]]
    print 'Document-Topic:\n'
    pprint(doc_topic)
    # for doc_topic in lda.get_document_topics(corpus_tfidf):
    #     print doc_topic
    # for topic_id in range(num_topics):
    #     print 'Topic', topic_id
        # pprint(lda.get_topic_terms(topicid=topic_id))#获取某主题对应的关键词列表：List（词汇编码，概率）
        # pprint(lda.show_topic(topic_id))#显示某主题的关键词列表:List(词汇，概率)
    # similarity = similarities.MatrixSimilarity(lda[corpus_tfidf]) #文档相似度矩阵
    # print 'Similarity:'
    # pprint(list(similarity))

    #新实现版本LDA:HDA
    # hda = models.HdpModel(corpus_tfidf, id2word=dictionary)
    # topic_result = [a for a in hda[corpus_tfidf]]
    # print '\n\nUSE WITH CARE--\nHDA Model:'
    # pprint(topic_result)
    # print 'HDA Topics:'
    # print hda.print_topics(num_topics=2, num_words=5)
