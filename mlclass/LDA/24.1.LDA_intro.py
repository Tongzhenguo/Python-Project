# !/usr/bin/python
# -*- coding:utf-8 -*-

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
    print 'Text = '
    pprint(texts)

    dictionary = corpora.Dictionary(texts)
    V = len(dictionary)
    corpus = [dictionary.doc2bow(text) for text in texts]
    # corpus_tfidf = models.TfidfModel(corpus)[corpus]
    corpus_tfidf = corpus

    print 'TF-IDF:'
    for c in corpus_tfidf:
        print c

    print '\nLSI Model:'
    lsi = models.LsiModel(corpus_tfidf, num_topics=2, id2word=dictionary)
    topic_result = [a for a in lsi[corpus_tfidf]]
    pprint(topic_result)
    print 'LSI Topics:'
    pprint(lsi.print_topics(num_topics=2, num_words=5))
    similarity = similarities.MatrixSimilarity(lsi[corpus_tfidf])   # similarities.Similarity()
    print 'Similarity:'
    pprint(list(similarity))

    print '\nLDA Model:'
    num_topics = 2
    lda = models.LdaModel(corpus_tfidf, num_topics=num_topics, id2word=dictionary,
                          alpha='auto', eta='auto', minimum_probability=0.001)
    doc_topic = [doc_t for doc_t in lda[corpus_tfidf]]
    print 'Document-Topic:\n'
    pprint(doc_topic)
    for doc_topic in lda.get_document_topics(corpus_tfidf):
        print doc_topic
    for topic_id in range(num_topics):
        print 'Topic', topic_id
        # pprint(lda.get_topic_terms(topicid=topic_id))
        pprint(lda.show_topic(topic_id))
    similarity = similarities.MatrixSimilarity(lda[corpus_tfidf])
    print 'Similarity:'
    pprint(list(similarity))

    hda = models.HdpModel(corpus_tfidf, id2word=dictionary)
    topic_result = [a for a in hda[corpus_tfidf]]
    print '\n\nUSE WITH CARE--\nHDA Model:'
    pprint(topic_result)
    print 'HDA Topics:'
    print hda.print_topics(num_topics=2, num_words=5)
