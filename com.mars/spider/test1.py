# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup


def contents(web_url):  # 爬虫获取网页没啥好说的
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"}
    # 不加text返回的是response，加了返回的是字符串
    html = requests.get(url=web_url, headers=header).text
    soup = BeautifulSoup(html, "lxml")
    tags = soup.select('.tagCol > tbody > tr > td > a')
    temps = []
    for tag in tags:
        temp = tag.get_text()
        if len(temp) > 0:
            temps.append(temp)
    print(temps)


if __name__ == '__main__':
    contents('https://book.douban.com/tag/?view=cloud')
