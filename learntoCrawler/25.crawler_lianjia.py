# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
import csv

reload(sys)
sys.setdefaultencoding('utf-8')


def not_empty(str):
    return str and str.strip()


if __name__ == '__main__':
    url_main = 'http://bj.lianjia.com'

    f = open(u'北京二手房20170308.csv', 'wb')
    f.write(unicode('\xEF\xBB\xBF', 'utf-8'))   # 文件头
    writer = csv.writer(f)
    writer.writerow(['区域', '小区名称', '户型', '面积', '价格(万)', '单价(元/平米)',
                     '性质', '朝向', '装修', '是否有电梯', '楼层', '建筑年代', '楼型'])
    res = requests.get('http://bj.lianjia.com/ershoufang')
    res = res.text.encode(res.encoding).decode('utf-8')
    soup = BeautifulSoup(res, 'html.parser')
    # print soup.prettify()
    districts = soup.find(name='div', attrs={'data-role':'ershoufang'}) # <div data-role="ershoufang">
    for district in districts.find_all(name='a'):
        print district['title'] #<a href="/ershoufang/dongcheng/" title="北京东城在售二手房 ">东城</a>
        district_name = district.text   # '东城', '西城', '朝阳', '海淀'......
        url = '%s%s' % (url_main, district['href'])
        # print url
        res = requests.get(url) #http://bj.lianjia.com/ershoufang/dongcheng/
        res = res.text.encode(res.encoding).decode('utf-8')
        soup = BeautifulSoup(res,'html.parser')
        # print soup.prettify()
        page = soup.find('div', {'class':'page-box house-lst-page-box'})
        if not page:    # 平谷区没有房源，直接返回
            continue
        total_pages = dict(eval(page['page-data']))['totalPage']    # 总页数
        # print total_pages
        for j in range(1, total_pages+1):
            url_page = '%spg%d/' % (url, j) #http://bj.lianjia.com/ershoufang/dongcheng/pg30/
            res = requests.get(url_page)
            res = res.text.encode(res.encoding).decode('utf-8')
            soup = BeautifulSoup(res, 'html.parser')
            # print soup.prettify()
            sells = soup.find(name='ul', attrs={'class':'sellListContent', 'log-mod':'list'})
            if not sells:
                continue
            # <a class="title" data-bl="list" data-el="ershoufang" data-log_index="1" href="XX" target="_blank">
            titles = soup.find_all(name='a', attrs={'class':'title', 'data-bl':'list', 'data-el':'ershoufang'})
            # <a data-el="region" data-log_index="1" href="X" target="_blank">
            regions = sells.find_all(name='a', attrs={'data-el':'region'})
            infos = sells.find_all(name='div', class_='houseInfo')      # <div class="houseInfo">
            infos2 = sells.find_all(name='div', class_='positionInfo')  # <div class="positionInfo">
            prices = sells.find_all(name='div', class_='totalPrice')    # <div class="totalPrice">
            unit_prices = sells.find_all(name='div', class_='unitPrice') # <div class="unitPrice" data-hid="X" data-price="X" data-rid="X">
            subways = sells.find_all(name='span', class_='subway')    # <span class="subway">
            taxs = sells.find_all(name='span', class_='taxfree')      # <span class="taxfree"> #这个没找到
            N = max(len(titles), len(regions), len(prices), len(unit_prices), len(subways), len(taxs), len(infos), len(infos2))
            # for title, region, price, unit_price, subway, tax, info, info2 in zip(titles, regions, prices, unit_prices, subways, taxs, infos, infos2):
            for i in range(N): #整合成N条记录
                room_type = area = orientation = decoration = elevator = floor = year = slab_tower = None
                title = titles[i] if len(titles) > i else None
                region = regions[i] if len(regions) > i else None
                price = prices[i] if len(prices) > i else None
                unit_price = unit_prices[i] if len(unit_prices) > i else None
                subway = subways[i] if len(subways) > i else None
                tax = taxs[i] if len(taxs) > i else None
                info = infos[i] if len(infos) > i else None
                info2 = infos2[i] if len(infos2) > i else None
                if title:
                    print 'Title: ', title.text
                if region:
                    region = region.text
                if price:
                    price = price.text
                    price = price[:price.find('万')]
                if unit_price:
                    unit_price = unit_price.span.text.strip()
                    unit_price = unit_price[:unit_price.find('元/平米')]
                    if unit_price.find('单价') != -1:
                        unit_price = unit_price[2:]
                if subway:
                    subway = subway.text.strip()
                if tax:
                    tax = tax.text.strip()
                if info:
                    info = info.text.split('|')
                    room_type = info[1].strip()     # 几室几厅
                    area = info[2].strip()          # 房屋面积
                    area = area[:area.find('平米')]
                    orientation = info[3].strip().replace(' ', '')   # 朝向
                    decoration = '-'
                    if len(info) > 4:       # 如果是车位，则该项为空
                        decoration = info[4].strip()    # 装修类型：简装、中装、精装、豪装、其他
                    elevator = '无'
                    if len(info) > 5:
                        elevator = info[5].strip()      # 是否有电梯：有、无
                if info2:
                    info2 = filter(not_empty, info2.text.split(' '))
                    floor = info2[0].strip()
                    info2 = info2[1]
                    year = info2[:info2.find('年')]
                    slab_tower = info2[info2.find('建')+1:]
                print district_name, region, room_type, area, price, unit_price, tax, orientation, decoration, elevator, floor, year, slab_tower
                writer.writerow([district_name, region, room_type, area, price, unit_price, tax, orientation, decoration, elevator, floor, year, slab_tower])
                # break
            # break
        # break
    f.close()
