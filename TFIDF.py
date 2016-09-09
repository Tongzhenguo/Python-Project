import math
import nltk as nltk


__author__ = 'YYT'
#TF-IDFµÄÊµÏÖ
def ComputeFreq(wordlist, text):
    result = []
    for word in wordlist:
        countword = text.count(word)
        texted = nltk.word_tokenize(text)
        length = len(texted)
        freq = countword/length
        temp = {}
        temp['word'] = word
        temp['freq'] = freq
        #print freq
        result.append(temp)
    return result
def Computetfidf(wordfreq, corpus):
    result = []
    for item in wordfreq:
        word = item['word']
        tf = item['freq']
        dlength = len(corpus)
        count = 1
        for line in corpus:
            if line.find(word)!=-1:
                count = count+1
        idf = math.log10(dlength/count)
        tfidf = tf * idf
        temp = {}
        temp['word'] = word
        temp['tfidf'] = tfidf
        result.append(temp)
    result.sort(lambda x,y : -cmp(x['tfidf'], y['tfidf']))
    return result
