# coding=utf-8
__author__ = 'arachis'

import csv
from urllib.parse import quote
import random
from time import sleep

import pandas as pd
from bs4 import BeautifulSoup
import requests


def doJob(id,yyt_song,yyt_artist):
    yyt_song = yyt_song.lower()
    yyt_artist = yyt_artist.lower()

    """爬取yyt_artist的yyt_song的标签信息，返回结果集"""
    # print yyt_song,yyt_artist
    url = u'http://www.xiami.com/search?key='+quote(str(yyt_song+" "+yyt_artist))
    #加上代理ip池
    ip_list=['112.253.22.142:80','112.253.22.141:80','220.194.199.184:80']
    #使用一组ip调用random函数来随机使用其中一个ip     #参数是一个字典{'类型':'代理ip:端口号'}
    proxies = {'http':random.choice(ip_list)}
    #伪装头
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
    print(url)
    res = requests.request('POST',url,timeout=60,headers=header)

    res = res.text.encode(res.encoding).decode('utf8')
    soup = BeautifulSoup(res, 'html.parser')
    music = soup.find(name='div', attrs={'class': 'search_result_box'})
    # print music
    track_list = music.find(name='table',attrs={"class":"track_list"})
    # print track_list
    if( not track_list ):#没有数据，返回
        return
    results = track_list.find_all(name='tbody')
    # print results
    cur_first_song = ""
    cur_first_artist = ""
    cur_first_songid = ""
    sign = 0 #匹配等级
    for result in results:
        # print result
        song_id = result.find(name="td",attrs={"class":"chkbox"}).input["value"]

        #
        song = result.find(name='a',attrs={'target':'_blank'})
        song_name = song["title"].lower()
        # type(song_title)
        artist = result.find(name="td", attrs={"class": "song_artist"}).a
        artist_name = artist["title"].lower()

        #定制匹配规则：优先匹配歌曲，然后匹配艺人
        if song_name == yyt_song and artist_name == yyt_artist:
            cur_first_song = song_name
            cur_first_artist = artist_name
            cur_first_songid = song_id
            sign = 3
            break
        elif song_name == yyt_song and artist_name !=  yyt_artist and sign < 2:
            cur_first_song = song_name
            cur_first_artist = artist_name
            cur_first_songid = song_id
            sign = 2
        elif (song_name.__contains__(yyt_song) or yyt_song.__contains__(song_name) ) and sign < 1:
            cur_first_song = song_name
            cur_first_artist = artist_name
            cur_first_songid = song_id
            sign = 1
        else:
            continue

    # 爬取对应歌曲的所有UGC标签，并写入csv文件
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
    record = [id,cur_first_song.replace(",",""),cur_first_artist.replace(",",""),cur_first_songid,tags.replace(",",""),str(sign)]
    print  ('id:'+str(id)+u",歌曲："+cur_first_song+u",艺人："+cur_first_artist+u",歌曲id: "+cur_first_songid+u",标签:"+tags+",匹配等级:"+str(sign))
    return record


def load_part(path):
    csv = pd.read_csv(path,header=None,encoding='utf-8')
    # print csv.values[0][0].decode('utf-8')
    return csv.values

if __name__ == "__main__":
    # record = doJob(1,'movin','タカチャ')
    jobID = 4
    i = 0
    path = 'data\part-'
    while( i< 337  ) :
        if i % 10 == jobID:
            # http://www.cnblogs.com/vamei/archive/2013/03/12/2954938.html
            idx = '%05d' % i
            part = load_part( path+idx )

            with open('yyt标签爬虫'+idx+'.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(['id','虾米歌曲', '虾米艺人', '虾米歌曲id', '虾米标签','匹配等级'])

                for ll in part:
                    id,yyt_song,yyt_artist = str(ll[0]),str(ll[1]),str(ll[2])
                    try:
                        record = doJob(id,yyt_song,yyt_artist)
                        if( record ):
                            writer.writerow(record)
                            # csvfile.close()
                        sleep(2)
                    except Exception as e:
                        if hasattr(e,"code"):
                            print(e.code)
                        if hasattr(e,"reason"):
                            print
                            var = e.reason
                            print
                        print("Connection refused by the server..")
                        print("Let me sleep for 5 seconds")
                        sleep(5)
                        continue
            csvfile.close()
        i += 1




