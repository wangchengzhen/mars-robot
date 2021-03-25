# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup


# 爬虫获取网页
def soup(web_url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"}
    # 不加text返回的是response，加了返回的是字符串
    html = requests.get(url=web_url, headers=header).text
    html_soup = BeautifulSoup(html, features="html.parser")
    return html_soup
