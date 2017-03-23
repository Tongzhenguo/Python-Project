# coding=utf-8
__author__ = 'arachis'

import csv
from urllib import quote
import sys
import random
from time import sleep

import pandas as pd
from bs4 import BeautifulSoup
import requests

reload(sys)
sys.setdefaultencoding('utf-8')


def doJob(id,yyt_song,yyt_artist):
    yyt_song = yyt_song.lower()
    yyt_artist = yyt_artist.lower()

    """爬取yyt_artist的yyt_song的标签信息，返回结果集"""
    # print yyt_song,yyt_artist
    url = u'http://www.xiami.com/search?key='+quote(str(yyt_song+" "+yyt_artist))
    #加上代理ip池
    ip_list=['192.168.1.199:10086','121.232.146.174:9000','121.232.147.153:9000']
    #使用一组ip调用random函数来随机使用其中一个ip     #参数是一个字典{'类型':'代理ip:端口号'}
    proxies = {'http':random.choice(ip_list)}
    #伪装头
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    print url
    res = requests.request('POST',url,timeout=60,headers=header)

    res = res.text.encode(res.encoding).decode('utf8')
    soup = BeautifulSoup(res, 'html.parser')
    track_list = soup.find(name='table',attrs={"class":"track_list"})
    results = track_list.find_all(name="tr",attrs={"class":" "}) #唯一定位
    # print results
    cur_first_song = ""
    cur_first_artist = ""
    cur_first_songid = ""
    for result in results:
        # print result
        song_id = result.find(name="td",attrs={"class":"chkbox"}).input["value"]

        song_name = result.find(name="td", attrs={"class": "song_name"}).a
        song_title = song_name["title"].lower()
        # type(song_title)
        artist = result.find(name="td", attrs={"class": "song_artist"}).a
        artist_name = artist["title"].lower()

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
        cur_first_songid = song_id
    if( cur_first_song == "" ):
        return

    #爬取对应歌曲的所有UGC标签，并写入csv文件
    url_moretags = "http://www.xiami.com/song/moretags/id/"+cur_first_songid
    moretags_page = requests.request('POST',url_moretags,timeout=60,headers=header)
    moretags_page = moretags_page.text.encode(moretags_page.encoding).decode('utf-8')
    soup = BeautifulSoup(moretags_page, 'html.parser')
    tag_cloud = soup.find(name='div', attrs={"class": "tag_cloud"})
    song_tags = ""
    if( tag_cloud ):
        song_tags = tag_cloud.find_all(name="a")
    # print song_tags
    tags = ""
    split = "@@@"
    for tag in song_tags:#http://cuiqingcai.com/1319.html
        tags += str(tag.string).replace("@","") +split
    tags = tags[:len(tags)-3]
    record = [id,cur_first_song.replace(",",""),cur_first_artist.replace(",",""),cur_first_songid,tags.replace(",","")]
    print  ('id:'+id+u",歌曲："+cur_first_song+u",艺人："+cur_first_artist+u",歌曲id: "+cur_first_songid+u",标签:"+tags).encode()
    return record


def load_part(path):
    csv = pd.read_csv(path,header=None,encoding='utf-8')
    # print csv.values[0][0].decode('utf-8')
    return csv.values

if __name__ == "__main__":
    jobID = 0
    i = 0
    path = 'part-' #注意：这里要修改成你的目录
    while( i< 337 ) :
        if  i % 10 == jobID :
            # http://www.cnblogs.com/vamei/archive/2013/03/12/2954938.html
            idx = '%05d' % i
            part = load_part( path+idx )

            f = open(u'yyt标签爬虫'+idx+'.csv', 'wb')
            f.write(unicode('\xEF\xBB\xBF', 'utf-8'))   # 文件头
            writer = csv.writer(f)
            writer.writerow(['id','虾米歌曲', '虾米艺人', '虾米歌曲id', '虾米标签'])
            for ll in part:
                id,yyt_song,yyt_artist = str(ll[0]).decode('utf-8'),str(ll[1]).decode('utf-8'),str(ll[2]).decode('utf-8')
                # print yyt_song,yyt_artist
                try:
                    record = doJob(id,yyt_song,yyt_artist)
                    if( record ):
                        writer.writerow(record)
                    sleep(2)
                except:
                    print("Connection refused by the server..")
                    print("Let me sleep for 5 seconds")
                    sleep(5)
                    continue
            f.close()
        i += 1




