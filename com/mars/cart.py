# -*- coding: UTF-8 -*-
import requests


def add(shopId, itemId):
    url = 'http://cart.kongfz.com/jsonp/add/?shopId=' + str(shopId) + '&itemId=' + str(itemId) + '&num=1'
    headers = {
        'Cookie': 'shoppingCartSessionId=30fb6fa52460506786bbba4c92baede7; utm_source=101002001000; kfz_uuid=219068a5-b308-45eb-bfeb-83c36f3e3f0e; reciever_area=1006000000; acw_tc=276077a416160379075954875e3d4009027d389b77bdb1aa90495c3018c2cf; PHPSESSID=9ae0a6d21fc5953a108b519be14ef965e0a1b647; kfz_trace=219068a5-b308-45eb-bfeb-83c36f3e3f0e|8132287|8460ded41617c906|101002001000; TY_SESSION_ID=03a81ab9-0ada-4a9d-a852-aa0f3ba0c087; Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c=1615618604,1615795222,1615966544,1616037916; Hm_lvt_33be6c04e0febc7531a1315c9594b136=1615618604,1615795222,1615966544,1616037916; Hm_lpvt_33be6c04e0febc7531a1315c9594b136=1616037934; Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c=1616037934',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"}
    res = requests.get(url, headers=headers)
    if res.text.index('1') > 0:
        print("Add cart success")


if __name__ == '__main__':
    add(1, 2)
