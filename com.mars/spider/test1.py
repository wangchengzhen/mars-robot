# -*- coding: UTF-8 -*-
import requests
from com.mars.html import soup


def contents(web_url):  # 爬虫获取网页没啥好说的
    html_soup = soup(web_url)
    tags = html_soup.select('.tagCol > tbody > tr > td > a')
    temps = []
    for tag in tags:
        temp = tag.get_text()
        if len(temp) > 0:
            temps.append(temp)
    return temps


if __name__ == '__main__':
    contents('https://book.douban.com/tag/?view=cloud')
