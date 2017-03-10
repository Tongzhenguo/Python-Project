# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
from gensim import corpora, models, similarities
from pprint import pprint
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import re
import pandas as pd
import jieba

# import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def load_stopword():
    f_stop = open('24.stopword.txt')
    sw = [line.strip() for line in f_stop]
    f_stop.close()
    return sw


def clean_info(info):
    replace_str = (('\n', ''), ('\r', ''), (',', '，'), ('表情', ''))
    for rs in replace_str:
        info = info.replace(rs[0], rs[1])

    at_pattern = re.compile(r'(@.* )')
    at = re.findall(pattern=at_pattern, string=info)
    for a in at:
        info = info.replace(a, '')
    idx = info.find('@')
    if idx != -1:
        info = info[:idx]
    return info


def regularize_data():
    time_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{1,2}:\d{1,2}:\d{1,2}')
    qq_pattern1 = re.compile(r'([1-9][0-9]{4,})')    # QQ号最小是10000
    qq_pattern2 = re.compile(r'(\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*)')
    f = open('《机器学习》升级版III.txt')
    f_output = open('QQ_chat.csv', mode='w')
    f_output.write('QQ,Time,Info\n')
    qq = chat_time = info = ''
    for line in f:
        line = line.strip()
        if line:
            t = re.findall(pattern=time_pattern, string=line)
            qq1 = re.findall(pattern=qq_pattern1, string=line)
            qq2 = re.findall(pattern=qq_pattern2, string=line)
            if (len(t) >= 1) and ((len(qq1) >= 1) or (len(qq2) >= 1)):
                if info:
                    info = clean_info(info)
                    if info:
                        info = '%s,%s,%s\n' % (qq, chat_time, info)
                        f_output.write(info)
                        info = ''
                if len(qq1) >= 1:
                    qq = qq1[0]
                else:
                    qq = qq2[0][0]
                chat_time = t[0]
            else:
                info += line
    f.close()
    f_output.close()


def load_stopwords():
    stopwords = set()
    f = open('24.stopword.txt')
    for w in f:
        stopwords.add(w.strip().decode('GB18030'))
    f.close()
    return stopwords


def segment():
    stopwords = load_stopwords()
    data = pd.read_csv('QQ_chat.csv', header=0)
    for i, info in enumerate(data['Info']):
        info_words = []
        words = jieba.cut(info)
        for word in words:
            if word not in stopwords:
                info_words.append(word.encode('utf-8'))
        if info_words:
            data.iloc[i, 2] = ' '.join(info_words)
        else:
            data.iloc[i, 2] = np.nan
    data.dropna(axis=0, how='any', inplace=True)
    data.to_csv('QQ_chat_segment.csv', sep=',', header=True, index=False)


def combine():
    data = pd.read_csv('QQ_chat_segment.csv', header=0)
    data['QQ'] = pd.Categorical(data['QQ']).codes
    f_output = open('QQ_chat_result.csv', mode='w')
    f_output.write('QQ,Info\n')
    for qq in data['QQ'].unique():
        info = ' '.join(data[data['QQ'] == qq]['Info'])
        str = '%s,%s\n' % (qq, info)
        f_output.write(str)
    f_output.close()


def lda():
    np.set_printoptions(linewidth=300)
    data = pd.read_csv('QQ_chat_result.csv', header=0)
    texts = []
    for info in data['Info']:
        texts.append(info.decode('utf-8').split(' '))
    M = len(texts)
    print '文档数目：%d个' % M
    # pprint(texts)

    print '正在建立词典 --'
    dictionary = corpora.Dictionary(texts)
    V = len(dictionary)
    print '正在计算文本向量 --'
    corpus = [dictionary.doc2bow(text) for text in texts]
    print '正在计算文档TF-IDF --'
    t_start = time.time()
    corpus_tfidf = models.TfidfModel(corpus)[corpus]
    print '建立文档TF-IDF完成，用时%.3f秒' % (time.time() - t_start)
    print 'LDA模型拟合推断 --'
    num_topics = 20
    t_start = time.time()
    lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dictionary,
                          alpha=0.001, eta=0.02, minimum_probability=0,
                          update_every=1, chunksize=1000, passes=20)
    print u'LDA模型完成，训练时间为\t%.3f秒' % (time.time() - t_start)
    # # 所有文档的主题
    # doc_topic = [a for a in lda[corpus_tfidf]]
    # print 'Document-Topic:\n'
    # pprint(doc_topic)

    num_show_term = 7  # 每个主题显示几个词
    print u'每个主题的词分布：'
    for topic_id in range(num_topics):
        print u'主题#%d：\t' % topic_id,
        term_distribute_all = lda.get_topic_terms(topicid=topic_id)
        term_distribute = term_distribute_all[:num_show_term]
        term_distribute = np.array(term_distribute)
        term_id = term_distribute[:, 0].astype(np.int)
        for t in term_id:
            print dictionary.id2token[t],
        print u'\n概率：\t', term_distribute[:, 1]

    # 随机打印某10个文档的主题
    np.set_printoptions(linewidth=200, suppress=True)
    num_show_topic = 10  # 每个文档显示前几个主题
    print u'10个用户的主题分布：'
    doc_topics = lda.get_document_topics(corpus_tfidf)  # 所有文档的主题分布
    idx = np.arange(M)
    np.random.shuffle(idx)
    idx = idx[:10]
    for i in idx:
        topic = np.array(doc_topics[i])
        topic_distribute = np.array(topic[:, 1])
        # print topic_distribute
        topic_idx = topic_distribute.argsort()[:-num_show_topic - 1:-1]
        print (u'第%d个用户的前%d个主题：' % (i, num_show_topic)), topic_idx
        print topic_distribute[topic_idx]
    # 显示着10个文档的主题
    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(12, 9), facecolor='w')
    for i, k in enumerate(idx):
        ax = plt.subplot(5, 2, i + 1)
        topic = np.array(doc_topics[i])
        topic_distribute = np.array(topic[:, 1])
        ax.stem(topic_distribute, linefmt='g-', markerfmt='ro')
        ax.set_xlim(-1, num_topics + 1)
        ax.set_ylim(0, 1)
        ax.set_ylabel(u"概率")
        ax.set_title(u"用户 {}".format(k))
        ax.grid(b=True)
    plt.xlabel(u"主题", fontsize=14)
    plt.suptitle(u'用户的主题分布', fontsize=18)
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.show()

    # 计算各个主题的强度
    print u'\n各个主题的强度:\n'
    topic_all = np.zeros(num_topics)
    doc_topics = lda.get_document_topics(corpus_tfidf)  # 所有文档的主题分布
    for i in np.arange(M):  # 遍历所有文档
        topic = np.array(doc_topics[i])
        topic_distribute = np.array(topic[:, 1])
        topic_all += topic_distribute
    topic_all /= M  # 平均
    idx = topic_all.argsort()
    topic_sort = topic_all[idx]
    print topic_sort
    plt.figure(facecolor='w')
    plt.stem(topic_sort, linefmt='g-', markerfmt='ro')
    plt.xticks(np.arange(idx.size), idx)
    plt.xlabel(u"主题", fontsize=14)
    plt.ylabel(u"主题出现概率", fontsize=14)
    plt.title(u'主题强度', fontsize=18)
    plt.grid(b=True, axis='both')
    plt.show()


if __name__ == '__main__':
    # regularize_data()
    # segment()
    # combine()
    lda()
