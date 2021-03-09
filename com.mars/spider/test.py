# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup
import pymysql
import time

ids = []


# 格式化2021-01-01 12:00:00
def local():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def conn():
    return pymysql.connect(
        "localhost",
        "root",
        "pa$$w0rd",
        "mars-robot",
        charset='utf8'
    )


def query(sql):
    db = conn()
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        print("Error: unable to query data")
    db.commit()
    db.close


def insert(sql):
    db = conn()
    cursor = db.cursor()
    # print('SQL:' + sql)
    try:
        cursor.execute(sql)
    except:
        print("Error: unable to insert data")
    db.commit()
    db.close


def soup(web_url):  # 爬虫获取网页没啥好说的
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"}
    # 不加text返回的是response，加了返回的是字符串
    html = requests.get(url=web_url, headers=header).text
    html_soup = BeautifulSoup(html, "lxml")
    return html_soup


def books(web_url):
    target_soup = soup(web_url)
    book_list = []
    for item in target_soup.select('.nbg'):
        book_list.append(item['href'])
    return book_list


def replaces(value):
    return value.replace(' ', '').replace(' ', '')


def Id(target_url):
    return re.sub(r'\D', '', target_url)


def country(attr):
    attrs = []
    if attr.find('[') == -1:
        attrs.append('中')
        attrs.append(attr)
    else:
        attrs.append(attr.split('[')[1].split(']')[0])
        attrs.append(attr.split('[')[1].split(']')[1])
    return attrs


def save(params):
    sql = f"INSERT INTO t_book (id, `title`, cover_image, score, comments, country, author, press, " \
          f"translator, edition_date, price, page_num, isbn, gmt_create, gmt_modified) VALUES ( "
    for param in params:
        sql = sql + "'" + str(param) + "',"
    sql = sql[:-1] + ")"
    insert(sql)


def get_book(book_url):  # 爬虫获取网页没啥好说的
    book_soup = soup(book_url)
    # 内容
    content = book_soup.find_all(id='info')[0]
    # 标题
    title = book_soup.find_all(property='v:itemreviewed')[0].get_text()
    # 评分
    score = book_soup.find_all(property='v:average')[0].get_text()
    # 评价人数
    comments = book_soup.find_all(property='v:votes')[0].get_text()
    # 封面
    cover_image = book_soup.find_all(rel='v:photo')[0]['src']

    # 去除空格,在用换行符分割成list
    temps = replaces(content.get_text()).split('\n')
    info = []
    for temps_index in range(len(temps)):
        if temps_index > 0:
            if temps[temps_index].find(':') == -1:
                info[-1] = info[-1] + temps[temps_index]
            else:
                info.append(temps[temps_index])
        else:
            info.append(temps[temps_index])

    params = [Id(book_url), title, cover_image, replaces(score), comments, '', '', '', '', '', '', '', '', local(),
              local()]
    for i in info:
        if i.find('作者') > -1:
            author = replaces(i.split(':')[1])
            params[5] = country(author)[0]
            params[6] = country(author)[1]
        if i.find('出版社') > -1:
            params[7] = replaces(i.split(':')[1])
        if i.find('译者') > -1:
            params[8] = replaces(i.split(':')[1])
        if i.find('出版年') > -1:
            params[9] = replaces(i.split(':')[1])
        if i.find('定价') > -1:
            params[10] = re.sub('[^0-9.]', '', i.split(':')[1])
        if i.find('页数') > -1:
            params[11] = replaces(i.split(':')[1])
        if i.find('ISBN') > -1:
            params[12] = replaces(i.split(':')[1])
    print(params)
    save(params)


if __name__ == '__main__':
    sql = f'select id from t_book'
    temps = list(query(sql))
    for temp_index in range(0, len(temps)):
        ids.append(re.sub(r'\D', '', str(temps[temp_index])))

    for index in range(0, 100, 20):
        url = 'https://book.douban.com/tag/%E5%A4%96%E5%9B%BD%E6%96%87%E5%AD%A6?start=' + str(index) + '&type=T'
        # 160-980
        # url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=' + str(index) + '&type=T'
        book = books(url)
        print(book)
        for book_url in book:
            book_id = re.sub(r'\D', '', book_url)
            try:
                ids.index(book_id)
            except ValueError:
                print(local() + ' >>>>>>>>>>>>>>>>>>>>>>')
                get_book(book_url)
                ids.append(book_id)
                time.sleep(30)
