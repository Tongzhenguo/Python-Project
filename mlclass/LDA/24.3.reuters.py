# !/usr/bin/python
# -*- coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import lda
import lda.datasets
from pprint import pprint


if __name__ == "__main__":
    # document-term matrix
    X = lda.datasets.load_reuters()
    print("type(X): {}".format(type(X)))
    print("shape: {}\n".format(X.shape))
    print(X[:10, :10])

    # the vocab
    vocab = lda.datasets.load_reuters_vocab()
    print("type(vocab): {}".format(type(vocab)))
    print("len(vocab): {}\n".format(len(vocab)))
    print(vocab[:10])

    # titles for each story
    titles = lda.datasets.load_reuters_titles()
    print("type(titles): {}".format(type(titles)))
    print("len(titles): {}\n".format(len(titles)))
    pprint(titles[:10])

    print 'LDA start ----'
    topic_num = 20
    model = lda.LDA(n_topics=topic_num, n_iter=500, random_state=1)
    model.fit(X)

    # topic-word
    topic_word = model.topic_word_
    print("type(topic_word): {}".format(type(topic_word)))
    print("shape: {}".format(topic_word.shape))
    print(vocab[:5])
    print(topic_word[:, :5])

    # Print Topic distribution
    n = 7
    for i, topic_dist in enumerate(topic_word):
        topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n + 1):-1]
        print('*Topic {}\n- {}'.format(i, ' '.join(topic_words)))

    # Document - topic
    doc_topic = model.doc_topic_
    print("type(doc_topic): {}".format(type(doc_topic)))
    print("shape: {}".format(doc_topic.shape))
    for i in range(10):
        topic_most_pr = doc_topic[i].argmax()
        print(u"文档: {} 主题: {} value: {}".format(i, topic_most_pr, doc_topic[i][topic_most_pr]))

    mpl.rcParams['font.sans-serif'] = [u'SimHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # Topic - word
    plt.figure(figsize=(8, 9))
    # f, ax = plt.subplots(5, 1, sharex=True)
    for i, k in enumerate([0, 5, 9, 14, 19]):
        ax = plt.subplot(5, 1, i+1)
        ax.plot(topic_word[k, :], 'r-')
        ax.set_xlim(-50, 4350)   # [0,4258]
        ax.set_ylim(0, 0.08)
        ax.set_ylabel(u"概率")
        ax.set_title(u"主题 {}".format(k))
    plt.xlabel(u"词", fontsize=14)
    plt.tight_layout()
    plt.suptitle(u'主题的词分布', fontsize=18)
    plt.subplots_adjust(top=0.9)
    plt.show()

    # Document - Topic
    plt.figure(figsize=(8, 9))
    # f, ax= plt.subplots(5, 1, figsize=(8, 6), sharex=True)
    for i, k in enumerate([1, 3, 4, 8, 9]):
        ax = plt.subplot(5, 1, i+1)
        ax.stem(doc_topic[k, :], linefmt='g-', markerfmt='ro')
        ax.set_xlim(-1, topic_num+1)
        ax.set_ylim(0, 1)
        ax.set_ylabel(u"概率")
        ax.set_title(u"文档 {}".format(k))
    plt.xlabel(u"主题", fontsize=14)
    plt.suptitle(u'文档的主题分布', fontsize=18)
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.show()
