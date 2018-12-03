# -*- coding: utf-8 -*-
import requests
from requests.exceptions import RequestException
import re
import json
import MySQLdb
import time
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
    pattern = re.compile('<div class="channel-detail movie-item-title" title="(.*?)">.*?movieId:(.*?)}"', re.S)

    items = re.findall(pattern, html)

    print(items)
    for item in items:
        yield {
            'id': item[1],
            'title': item[0],
        }


def main():
    db = MySQLdb.connect('127.0.0.1', 'root', sys.argv[1], 'shengxi_v2')
    cursor = db.cursor()
    url = 'http://maoyan.com/films?showType=2'

    cursor.execute("truncate table sx_maoyan")

    for i in range(0, 9):
        offset = i * 30
        weburl = url + '&offset=' + offset.__str__()
        print(weburl)
        html = get_one_page(weburl)
        for item in parse_one_page(html):
            print(item)
            insert_table(item, db, cursor)


def insert_table(item, db, cursor):
    upsql = "insert into sx_maoyan set my_id='%s',movie_title='%s',movie_alias='%s'," \
            "movie_tag ='%s',movie_poster='%s',movie_intro='%s',movie_area='%s',movie_type='%s', created_at = %d" \
            % (str(item['id']), str(item['title']), '', json.dumps([]), '', '', json.dumps([]), json.dumps([]),
               int(time.time()))
    print(upsql)
    cursor.execute(upsql)
    db.commit()


if __name__ == '__main__':
    main()
