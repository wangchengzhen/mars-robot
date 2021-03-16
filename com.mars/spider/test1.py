# -*- coding: UTF-8 -*-
import re
import time
from com.mars.db import queryAll
from com.mars.db import insert
from com.mars.html import soup

ids = []
errorIds = []


# 格式化2021-01-01 12:00:00
def local():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def contents(web_url):  # 爬虫获取网页没啥好说的
    html_soup = soup(web_url)
    tags = html_soup.select('.tagCol > tbody > tr > td > a')
    temps = []
    for tag in tags:
        temp = tag.get_text()
        if len(temp) > 0:
            temps.append(temp)
    return temps


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
    attrs = ['', attr]
    if attr.find('[') == -1 and attr.find('(') == -1 and attr.find('【') == -1 and attr.find('（') == -1 :
        return attrs
    if attr.find('[') > -1:
        attrs[0] = attr.split('[')[1].split(']')[0]
        attrs[1] = attr.split('[')[1].split(']')[1]
    if attr.find('(') > -1:
        attrs[0] = attr.split('(')[1].split(')')[0]
        attrs[1] = attr.split('(')[1].split(')')[1]
    if attr.find('【') > -1:
        attrs[0] = attr.split('【')[1].split('】')[0]
        attrs[1] = attr.split('【')[1].split('】')[1]
    if attr.find('（') > -1:
        attrs[0] = attr.split('（')[1].split('）')[0]
        attrs[1] = attr.split('（')[1].split('）')[1]
    return attrs


def save(params):
    insert_sql = f"INSERT INTO t_book (id, `title`, cover_image, score, comments, country, author, press, " \
                 f"translator, edition_date, price, page_num, isbn, gmt_created, gmt_modified) VALUES ( "
    for param in params:
        insert_sql = insert_sql + "'" + str(param) + "',"
    insert_sql = insert_sql[:-1] + ")"
    result = insert(insert_sql)
    if result == 0:
        errorIds.append(params[0])
        print('Error:', errorIds)


def get_book(bookUrl):  # 爬虫获取网页没啥好说的
    book_soup = soup(bookUrl)
    # 内容
    content = book_soup.find_all(id='info')[0]
    # 标题
    title = book_soup.find_all(property='v:itemreviewed')[0].get_text()
    # 评分
    score = "0"
    scores = book_soup.find_all(property='v:average')
    if len(scores) > 0:
        score = replaces(str(scores[0].get_text()))
        if len(score) == 0:
            score = "0"

    # 评价人数
    comments = 0
    comment = book_soup.find_all(property='v:votes')
    if len(comment) > 0:
        comments = comment[0].get_text()
        if len(comments) == 0:
            comments = 0
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

    params = [Id(bookUrl), title, cover_image, score, comments, '', '', '', '', '', 0, 0, '',
              local(),
              local()]
    for i in info:
        if i.find('作者') > -1:
            author = replaces(i.split(':')[1])
            params[5] = country(author)[0]
            params[6] = country(author)[1].replace("'", "`")
        if i.find('出版社') > -1:
            params[7] = replaces(i.split(':')[1]).replace("'", "`")
        if i.find('译者') > -1:
            params[8] = replaces(i.split(':')[1])
        if i.find('出版年') > -1:
            params[9] = replaces(i.split(':')[1])
        if i.find('定价') > -1:
            params[10] = re.sub('[^0-9.]', '', i.split(':')[1])
        if i.find('页数') > -1:
            pageSize = re.sub('[^0-9]', '', i.split(':')[1])
            if pageSize == '':
                pageSize = '0'
            params[11] = pageSize
        if i.find('ISBN') > -1:
            params[12] = replaces(i.split(':')[1])
    print(params)
    save(params)


if __name__ == '__main__':
    get_book(f'https://book.douban.com/subject/35225413')
