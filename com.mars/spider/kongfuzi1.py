# -*- coding: UTF-8 -*-
import time
import requests
import json
from com.mars.mail import sendHtml
from com.mars.cart import add
from com.mars.db import queryAll, update


# 格式化2021-01-01 12:00:00
def local():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


# 格式化2021-01-01 12:00:00
def query(targetBook):
    url = 'http://search.kongfz.com/product_result/?key=' + targetBook[4] + \
          '&status=0&order=100&quality=85h&pagenum=1&ajaxdata=1&type=1&_=1615452347428'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
        'Cookie': 'shoppingCartSessionId=f61d09c070168f85cad4e73b152b5231; kfz_uuid=46775530-2d15-4807-8933-2398e517eec0; kfz-tid=de00874ac7a9536cf0a8e41bc5dce758; reciever_area=1006000000; PHPSESSID=0efab51bf53455d50b6c65055e599e3cc3f7bff4; utm_source=101002001000; token=4353cda13e1ad88731017974218ebfd7; acw_tc=2760774d16157952215221048e8ce3d872fa9f6d83f6f16baa213466a84b9d; TY_SESSION_ID=11fff9b7-94af-40c2-b89f-54f91d5480ae; Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c=1615618588,1615618598,1615618604,1615795222; Hm_lvt_33be6c04e0febc7531a1315c9594b136=1615618588,1615618598,1615618604,1615795222; kfz_trace=46775530-2d15-4807-8933-2398e517eec0|0|5e4305222fbd1621|101002001000; TINGYUN_DATA=%7B%22id%22%3A%22XMf0fX2k_0w%23nUhCMQN2SSk%22%2C%22n%22%3A%22WebAction%2FURI%2Fproduct%252Fsearch%252Fpc%252F%22%2C%22tid%22%3A%22206b5c0d8c61e2a%22%2C%22q%22%3A0%2C%22a%22%3A89%7D; Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c=1615795715; Hm_lpvt_33be6c04e0febc7531a1315c9594b136=1615795715; acw_sc__v2=604f180da8032f04f5db45fa6f480ade2bfe6b7a'}
    res = requests.get(url, headers=headers)
    items = json.loads(res.text)['data']['itemList']
    if len(items) > 0:
        print('%s: >>>>>>>>>>> 正在搜索的书籍：《%s》' % (local(), targetBook[1]))
        for item in items[targetBook[3]: -1]:
            # print(item['price'])
            if float(item['price']) <= targetBook[2]:
                content = "<a href='http://book.kongfz.com/%s/%s/'>跳转</a>" % (item['shopid'], item['itemid'])
                # 邮箱信息提示
                sendHtml('%s出现低价书' % targetBook[1], content)
                # 加入购物车
                add(item['shopid'], item['itemid'])
                # 放入待删除列表
                updateTarget(targetBook[0])
                print('\n')


# 格式化2021-01-01 12:00:00
def targets():
    sql = f"select * from t_book_target where is_enable = 1"
    return queryAll(sql)


def updateTarget(bookId):
    sql = f"update t_book_target set is_enable = 0 where id = " + str(bookId)
    return update(sql)


if __name__ == '__main__':
    # isbn/目标价格/搜索index/书名
    while 1:
        # 找书
        for book in list(targets()):
            query(book)

        # 休眠时间 1800s
        time.sleep(60 * 60 * 0.5)
        print('\n')
