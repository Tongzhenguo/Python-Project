# -*- coding:utf-8 -*-

import urllib2
import re
import os
import sys
from bs4 import BeautifulSoup
import httplib

reload(sys)
sys.setdefaultencoding('utf-8')


def write_file(url, path):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('gbk')
        # print content
        pattern = re.compile('<div class="post_content_main" id="epContentLeft">.*?<h1>(.*?)</h1>', re.S)
        title = re.findall(pattern=pattern, string=content)
        if not title:
            return
        title = title[0]
        # print title   # 标题
        pattern = re.compile('<p class="otitle">(.*?)<!-- AD200x300_2 -->', re.S)
        text = re.findall(pattern=pattern, string=content)
        # print text
        if not text:
            return
        text = text[0]
        soup = BeautifulSoup(text, 'html.parser')
        clear_text = ''
        for item in soup.find_all('p'):
            t = item.get_text()
            if t:
                clear_text += (t + '\n')
        # print clear_text    # 正文
        file_path = path + url[url.rfind('/')+1:url.rfind('.')] + '.txt'
        f = open(file_path, mode='w')
        f.write('原始链接：'+url+'\n\n')
        f.write(title+'\n\n')
        f.write(clear_text)
        f.close()
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason


def crawl_topic(url, topic):
    print '正在爬取主题：', topic
    print '链接：', url
    topic_path = main_dictionary+topic+'\\'
    if not os.path.exists(topic_path):
        os.mkdir(topic_path)
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        content = response.read().decode('gbk')
        # print content
        pattern = re.compile('<td class=".*?"><span>.*?</span><a href="(.*?)">(.*?)</a></td>')
        items = re.findall(pattern=pattern, string=content)
        pattern = re.compile('<td class=".*?"><a href="(.*?)">(.*?)</a></td>')
        items += re.findall(pattern=pattern, string=content)
        for i, (link, title) in enumerate(items):
            print link, title
            write_file(link, topic_path)
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
    print '\n\n\n\n'


if __name__ == '__main__':
    main_dictionary = '.\\Content\\'
    if not os.path.exists(main_dictionary):
        os.mkdir(main_dictionary)
    url = 'http://news.163.com/rank/'
    headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    try:
        print '建立连接'
        request = urllib2.Request(url, headers={})
        response = urllib2.urlopen(request)
        content = response.read().decode('gbk')
        # print content
        pattern = re.compile(u'<div class="list"><ul id="calendarList"><li></li></ul></div>'
                             u'.*?<div class="subNav">快速跳转：(.*?)<div class="area areabg1">', re.S)
        link_name = re.findall(pattern=pattern, string=content)[0]
        soup = BeautifulSoup(link_name, 'html.parser')
        for item in soup.find_all('a'):
            crawl_topic(item['href'], item.get_text())
            break
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason
    except httplib.IncompleteRead, e:
        print '---httplib.IncompleteRead---'
        print e
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason
