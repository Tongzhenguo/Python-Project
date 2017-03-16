# -*- coding:utf-8 -*-

import urllib2
import re
import os
import sys
import requests
from bs4 import BeautifulSoup


reload(sys)
sys.setdefaultencoding('utf-8')


def write_file(file_name, writer_name, agree, comment, postings):
    f = open(dictionary+file_name+'.txt', mode='w')
    f.write(writer_name+'\t'+agree+'\t'+comment+'\n')
    f.write(postings)
    f.close()


if __name__ == '__main__':
    dictionary = '.\\Qiubai\\'
    if not os.path.exists(dictionary):
        os.mkdir(dictionary)
    f_all = open(dictionary+'All.txt', mode='w')

    for page in range(1, 100):
        url = 'http://www.qiushibaike.com/hot/page/' + str(page)
        headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        # print url
        try:
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            print content
            # content = requests.get(url)
            # content = content.text.encode(content.encoding).decode('utf-8')
            pattern = re.compile('<div class="author clearfix">.*?<a href="/users/.*?/".*?'
                                 '<img src=".*? alt="(.*?)"/>.*?'
                                 '<a href="/article/(.*?)".*?<div class="content">.*?<span>(.*?)</span>'
                                 '.*?<span class="stats-vote"><i class="number">(.*?)</i>.*?</span>'
                                 '.*?<span class="stats-comments">.*?<a href="/article/.*?<i class="number">(.*?)</i>',
                                 re.S)
            items = re.findall(pattern, content)
            for i, item in enumerate(items):
                postings = item[2].replace('<br/>', '\n')
                print '发帖人ID：', item[0]
                print '帖子ID：', item[1]
                print '内容：', postings
                print '点赞：', item[3]
                print '评论数：', item[4]
                write_file(item[1], item[0], item[3], item[4], postings)
                f_all.write(item[0])
                f_all.write('\n')
                f_all.write(postings)
                f_all.write('\n\n')
        except urllib2.URLError, e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason
            break
    f_all.close()
