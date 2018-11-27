# 猫眼电影抓取,http://maoyan.com/
import requests
from requests.exceptions import RequestException
import re
import json
from selenium import webdriver
import time
import os
import MySQLdb


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
        '<div class="celebrity-type">.*演员.*?<span class="num">.*?<div class="info">.*?'
        'class="name">(.*?)</a>.*?div class="info">.*?class="name">(.*?)</a>.*?div class="info">.*?class="name">(.*?)</a>.*?div class="info">.*?class="name">(.*?)</a>',
        re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield {
            item[0].replace(' ', '').replace('\n', ''),
            item[1].replace(' ', '').replace('\n', ''),
            item[2].replace(' ', '').replace('\n', ''),
            item[3].replace(' ', '').replace('\n', ''),
        }


def main():
    db = MySQLdb.connect('192.168.31.100', 'root', '123456', 'shengxi_v2')

    cursor = db.cursor()
    sql = """select * from sx_maoyan  where id =253 order by id asc"""
    cursor.execute(sql)

    results = cursor.fetchall()
    for row in results:
        usql = "update sx_maoyan set movie_starring = '%s' where id = %d" % (json.dumps([]), row[0])
        cursor.execute(usql)
        db.commit()
        url = 'http://maoyan.com/films/' + str(row[1])
        print(url)

        html = get_one_page(url)
        for item in parse_one_page(html):
            print(item)
            upsql = "update sx_maoyan set movie_starring ='%s' where id = %d" % (
                json.dumps(list(item), ensure_ascii=False), row[0])

            cursor.execute(upsql)
            db.commit()


if __name__ == '__main__':
    main()
