# coding=utf-8
from urllib import quote
__author__ = 'arachis'

import pandas as pd
from bs4 import BeautifulSoup
import sys
import urllib2
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

# xaa = pd.read_csv('E:\pycharm\yytCrawler\\xaa.csv')
# print xaa.head(5)

url = 'http://www.xiami.com/search?key='
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
yyt_song = "那种女孩"
yyt_artist = "范晓萱"
res = requests.get(url+quote(yyt_song+" "+yyt_artist),headers=headers)
res = res.text.encode(res.encoding).decode('utf-8')
soup = BeautifulSoup(res, 'html.parser')
track_list = soup.find(name='table',attrs={"class":"track_list"})
results = track_list.find_all(name="tr",attrs={"class":" "}) #唯一定位
# print results
cur_first_song = ""
cur_first_artist = ""
cur_first_href = ""
cur_first_songid = ""
for result in results:
    # print result
    song_id = result.find(name="td",attrs={"class":"chkbox"}).input["value"]

    song_name = result.find(name="td", attrs={"class": "song_name"}).a
    href = song_name["href"]
    # print href
    song_title = song_name["title"]
    type(song_title)
    artist = result.find(name="td", attrs={"class": "song_artist"}).a
    artist_name = artist["title"]

    # print "song:"+song_title+" href:"+href+" artist:"+artist_name #song:那种女孩 href:http://www.xiami.com/song/Dzhc46b01 artist:范晓萱

    #定制匹配规则：优先匹配歌曲，然后匹配艺人
    if cur_first_song == "":
        cur_first_song = song_title
        if cur_first_artist == "":
            cur_first_artist = artist_name
        if artist_name ==  yyt_artist:
            cur_first_artist = artist_name
    if song_name == yyt_song:
        cur_first_song = song_title
        if cur_first_artist == "":
            cur_first_artist = artist_name
        if artist_name ==  yyt_artist:
            cur_first_artist = artist_name
    cur_first_href = href
    cur_first_songid = song_id
print "歌曲："+cur_first_song+",艺人："+cur_first_artist+",歌曲id: "+cur_first_songid

#爬取对应歌曲的所有UGC标签，并写入csv文件
url_moretags = "http://www.xiami.com/song/moretags/id/"
moretags_page = requests.get(url_moretags+cur_first_songid,headers=headers)
moretags_page = moretags_page.text.encode(moretags_page.encoding).decode('utf-8')
soup = BeautifulSoup(moretags_page, 'html.parser')
song_tags = soup.find(name='div',attrs={"class":"tag_cloud"}).find_all(name="a")
for tag in song_tags:

# print song_tags



