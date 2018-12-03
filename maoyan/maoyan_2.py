# -*- coding: utf-8 -*
import requests
from requests.exceptions import RequestException
import re
import json
import MySQLdb
import sys


def get_one_page(url):
    '''
    获取网页内容
    :param url: 网页地址
    :return: 网页内容
    '''
    try:
        # 获取页码内容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'  # 代理浏览器
                          + 'Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        }
        response = requests.get(url, headers=headers)
        # 通过状态判断是否获取成功
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    '''
      <div class="channel-detail movie-item-title" title="惊奇队长">
      <a href="/films/341139" target="_blank" data-act="movies-click" data-val="{movieId:341139}">惊奇队长</a>
    </div>
    :param html:
    :return:
    '''
    pattern = re.compile(
        '<img class="avatar" src="(.*?)".*?<h3 class="name">(.*?)</h3>.*?<div class="ename ellipsis">(.*?)</div>.*?<li class="ellipsis">(.*?)</li>.*?'
        '<li class="ellipsis">(.*?)</li>.*?<li class="ellipsis">(.*?)</li>.*?<span class="dra">(.*?)</span>',
        re.S)

    items = re.findall(pattern, html)

    for item in items:
        area = item[4].replace(' ', '').replace('\n', '')
        if '/' in area:
            areainfo = area.split('/')
            area = areainfo[0]
            length = areainfo[1][0:-2]
        else:
            length = 0

        yield {
            'image': item[0],
            'name': item[1],
            'ename': item[2],
            'type': item[3],
            'area': area,
            'length': length,
            'release': item[5][0:-4],
            'desc': item[6],
        }


def main():
    db = MySQLdb.connect('127.0.0.1', 'root', sys.argv[1], 'shengxi_v2')
    cursor = db.cursor()
    sql = """select * from sx_maoyan"""
    cursor.execute(sql)

    results = cursor.fetchall()
    for row in results:
        url = 'http://maoyan.com/films/' + str(row[1])
        print(url)
        html = get_one_page(url)
        print(html)
        if not html is None:
            for item in parse_one_page(html):
                upsql = "update sx_maoyan set movie_alias='%s',movie_poster='%s',`movie_type`='%s',movie_area='%s'," \
                        "`movie_len`='%s',release_at='%s',`movie_intro`='%s',movie_starring ='%s' where id = %d" \
                        % (item['ename'], item['image'], json.dumps(item['type'].split(','), ensure_ascii=False),
                           json.dumps(item['area'].split(','), ensure_ascii=False), item['length'],
                           item['release'],
                           item['desc'], json.dumps([], ensure_ascii=False), row[0])
                cursor.execute(upsql)
                db.commit()


if __name__ == '__main__':
    main()
