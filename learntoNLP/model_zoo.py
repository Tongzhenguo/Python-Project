# coding=utf-8
'''
    学习gensim
'''

import codecs
import logging
import re
from collections import namedtuple
import numpy as np
import jieba
import pandas as pd
from gensim import corpora
from gensim import matutils
from gensim import models
from gensim.models import Doc2Vec
from six import iteritems

re_han = re.compile("([\u4E00-\u9FD5]+)", re.U)
stop_words_path = "../../data/stop_words.txt"
dmp_tag_path = '../../data/dmp_tag.txt'
hot_words_path = '../../data/hot_words.csv'
mydict_path = '../../data/mydict.txt'
text_corpus_path = '../../data/mycorpus.txt'
text_corpus_shuf_path = '../../data/mycorpus_shuf.txt'
dictionary_path = '../../data/post.dict'
corpus_path = '../../cache/corpus.pkl'
tfidf_path = '../../model/tfidf.model'
lsi_path = '../../model/lsi.model'
lda_path = '../../model/model.lda'
hdp_path = '../../model/model.hdp'
vec_model = '../../model/word2vec.model'
batch_size = 10000
total_samples = 556197
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

jieba.dt.tmp_dir = '..\..\cache\\'
jieba.dt.cache_file = 'jieba.cache'
import os

stoplist = set()
with open(stop_words_path, 'rb') as f:
    while (True):
        word = f.readline().decode('utf-8')
        if word:
            if '\r\n' in word: word = word.replace('\r\n', '')
            stoplist.add(word)
        else:
            break
# data = pd.read_csv(text_corpus_path)
# data.sample(frac=1.0,random_state=666).to_csv(text_corpus_shuf_path,index=False,header=False,encoding='utf8')
def token_extract(text):
    han_list = []
    for i in jieba.cut(text, cut_all=False, HMM=True):
        if i in stoplist: continue
        if re_han.match(i): han_list.append(i)
    return ' '.join(han_list)

def make_corpus():
    dictionary = corpora.Dictionary(token_extract(line.decode('utf-8')).lower().split() for line in open(text_corpus_path, 'rb'))
    stoplist = set()
    with open(stop_words_path,'rb') as f:
        while(True):
            word = f.readline().decode('utf-8')
            if word:
                if '\r\n' in word:word = word.replace('\r\n','')
                stoplist.add( word )
            else:break
    # remove stop words and words that appear only once
    stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
                if stopword in dictionary.token2id]
    once_ids = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq <= 3]
    dictionary.filter_tokens(stop_ids + once_ids)  # remove stop words and words that appear only once
    dictionary.compactify()  # remove gaps in id sequence after words that were removed
    print(dictionary)
    dictionary.save(dictionary_path)
    #Corpus Streaming – One Document at a Time,doesn't load the corpus into memory!
    class MyCorpus(object):
        def __iter__(self):
            for line in open(text_corpus_path, 'rb'):
                # assume there's one document per line, tokens separated by whitespace
                yield dictionary.doc2bow(token_extract(line.decode('utf-8')).lower().split())
    corpus_memory_friendly = MyCorpus()  # doesn't load the corpus into memory!
    # corpus_memory_friendly
    corpus = []
    for vector in corpus_memory_friendly:  # load one vector into memory at a time
        corpus.append( vector )
    pd.to_pickle(corpus, corpus_path)
# make_corpus()

def trans_word2vec( hs=1,sg=1,size=100,window=5 ):
    # Corpus Streaming – One Document at a Time,doesn't load the corpus into memory!
    class MyCorpus(object):
        def __init__(self, dirname):
            self.dirname = dirname
        def __iter__(self):
            for line in open(text_corpus_path, 'rb'):
                # assume there's one document per line, tokens separated by whitespace
                yield token_extract(line.decode('utf-8')).split()
    corpus_memory_friendly = MyCorpus(text_corpus_path)
    other_sentences = MyCorpus(text_corpus_shuf_path)
    model = models.Word2Vec(iter=1,workers=4,hs=hs,sg=sg,size=size,window=window)
    model.build_vocab(corpus_memory_friendly)
    model.train(other_sentences, total_examples=total_samples, epochs=1)
    model.save('../../model/word2vec_{hs}_{sg}_{size}_{window}.model'.format(hs=hs,sg=sg,size=size,window=window ) )
# for h in [1,0]:
#     for sg in [1,0]:
#         for s in [100,300]:
#             for w in [5,15]:
#                 trans_word2vec(h,sg,s,w)

def d2v_train( hs,dm,size,window ):
    SentimentDocument = namedtuple('SentimentDocument', 'words tags')
    class Doc_list(object):
        def __init__(self,f):
            self.f = f
        def __iter__(self):
            for i,line in enumerate(codecs.open(self.f,encoding='utf8')):
                words = token_extract(line).split(' ')
                tags = [i]
                words = words[1:]
                yield SentimentDocument(words,tags)

    d2v = Doc2Vec(dm=dm, size=size, hs=hs,window=window, workers=4)
    doc_list = Doc_list(text_corpus_shuf_path)
    d2v.build_vocab(doc_list)
    d2v.train(doc_list, total_examples=total_samples, epochs=5)
    if dm == 1:
        path = '../../model/dm_d2v_%s_%s_%s' % (hs,size,window)
    else:
        path = '../../model/dbow_d2v_%s_%s_%s' % (hs, size, window)
    d2v.save(path)
# for h in [1,0]:
#     for dm in [1,0]:
#         for s in [100,300]:
#             for w in [5,15]:
#                 if h==1 and s ==100 and w == 5 and dm==1:
#                     continue
#                 d2v_train(h,dm,s,w)

def trans_lsi():#a latent space of a lower dimensionality
    dictionary = corpora.Dictionary.load(dictionary_path)
    corpus = pd.read_pickle(corpus_path)
    tfidf = models.TfidfModel(corpus)  # We cannot convert the entire corpus at the time of calling corpus_transformed = model[corpus],
    # the transformation is costly, serialize the resulting corpus to disk first and continue using that.
    corpus_tfidf = tfidf[corpus]  # tf-idf => L2 norm
    #target dimensionality of 200–500 is recommended as a “golden standard”
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=30)  # initialize an LSI transformation
    lsi.print_topics(30)
    corpus_lsi = lsi[corpus_tfidf]  # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
    i = 0
    for doc in corpus_lsi: # both bow->tfidf and tfidf->lsi transformations are actually executed here, on the fly
        i += 1
        if i % batch_size == 0:
            print(doc)
    tfidf.save( tfidf_path )
    lsi.save(lsi_path)  # same for tfidf, lda, ...
# trans_lsi()

def trans_lda():#a probabilistic extension of LSA (also called multinomial PCA),
    dictionary = corpora.Dictionary.load(dictionary_path)
    corpus = pd.read_pickle( corpus_path )
    tfidf = models.TfidfModel(corpus)  # We cannot convert the entire corpus at the time of calling corpus_transformed = model[corpus],
    # the transformation is costly, serialize the resulting corpus to disk first and continue using that.
    corpus_tfidf = tfidf[corpus]  # tf-idf 然后L2规范化
    lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=30)
    lda.print_topics(30)
    corpus_lda = lda[corpus_tfidf]  # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
    i = 0
    for doc in corpus_lda: # both bow->tfidf and tfidf->lsi transformations are actually executed here, on the fly
        i+= 1
        if i % batch_size == 0:
            print(doc)
    lda.save(lda_path)  # same for tfidf, lda, ...
# trans_lda()

def trans_hdp(): #a non-parametric bayesian method
    dictionary = corpora.Dictionary.load(dictionary_path)
    corpus = pd.read_pickle( corpus_path )
    tfidf = models.TfidfModel(corpus)  # We cannot convert the entire corpus at the time of calling corpus_transformed = model[corpus],
    # the transformation is costly, serialize the resulting corpus to disk first and continue using that.
    corpus_tfidf = tfidf[corpus]  # tf-idf 然后L2规范化
    hdp = models.HdpModel(corpus, id2word=dictionary,max_time=5*60)
    hdp.print_topics(30)
    corpus_hdp = hdp[corpus_tfidf]  # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi
    i = 0
    for doc in corpus_hdp: # both bow->tfidf and tfidf->lsi transformations are actually executed here, on the fly
        i+=1
        if i%batch_size==0:
            print(doc)
    hdp.save(hdp_path)  # same for tfidf, lda, ...


