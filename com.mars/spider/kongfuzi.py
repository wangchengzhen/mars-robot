# -*- coding: UTF-8 -*-
from com.mars.db import queryById
from com.mars.html import soup
from com.mars.cart import add
from com.mars.mail import send

ids = []


# 格式化2021-01-01 12:00:00
def book(shopId, pageNo):
    html_soup = soup('http://shop.kongfz.com/' + str(shopId) + '/all/0_50_0_0_' + str(pageNo) + '_sort_desc_0_0/')
    items = html_soup.select('.list-content > div')
    books = []
    for item in items[0:50]:
        books.append(str(item['itemid']) + ':' + str(item['isbn']))
    return books


def score(isbn):
    sql = 'select * from t_book where isbn = ' + str(isbn)
    # print(sql)
    item = queryById(sql)
    if item is None:
        print('本地书库未录入isbn:', isbn)
        return 0
    print('score:' + str(item[3]))
    print('comments:' + str(item[4]))
    if (float(item[3]) > 8.4 and int(item[4]) > 3000) or (float(item[3]) > 9 and int(item[4]) > 1000):
        print(item)
        if float(item[3]) > 10 and int(item[4]) > 10000:
            content = (str(item[1]) + '|' + str(item[3]) + '|' + str(item[4]))
            send(content)
        return 1
    else:
        return 0


def loop(start, limit, shopId):
    for index in range(start, limit, 1):
        books = book(shopId, index)
        for item in books:
            itemId = item.split(':')[0]
            isbn = item.split(':')[1]
            if len(isbn.strip()) > 0:
                temp = score(isbn)
                if temp == 1:
                    # 添加购物车
                    add(shopId, itemId)
        print('index: %s end' % index)
        print('\n')


if __name__ == '__main__':
    loop(0, 253, 23715)
