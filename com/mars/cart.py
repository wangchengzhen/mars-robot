# -*- coding: UTF-8 -*-
import requests


def add(shopId, itemId):
    url = 'http://cart.kongfz.com/jsonp/add/?shopId=' + str(shopId) + '&itemId=' + str(itemId) + '&num=1'
    headers = {
        'Cookie': 'shoppingCartSessionId=f61d09c070168f85cad4e73b152b5231; kfz_uuid=46775530-2d15-4807-8933-2398e517eec0; kfz-tid=de00874ac7a9536cf0a8e41bc5dce758; reciever_area=1006000000; PHPSESSID=0efab51bf53455d50b6c65055e599e3cc3f7bff4; token=b715b3527867fa61de666c9e1c55729b; utm_source=101002001000; kfz_trace=46775530-2d15-4807-8933-2398e517eec0|8132287|5e4305222fbd1621|101002001000; acw_tc=276077b716155952403104401ed11a5d826851c111de27d53fb96407bf618d; TY_SESSION_ID=5d32dbaf-51ab-4895-b155-34abacc576c5; Hm_lvt_bca7840de7b518b3c5e6c6d73ca2662c=1614912301,1615180111,1615357939,1615595245; Hm_lvt_33be6c04e0febc7531a1315c9594b136=1614912301,1615180111,1615357939,1615595245; Hm_lpvt_33be6c04e0febc7531a1315c9594b136=1615595252; Hm_lpvt_bca7840de7b518b3c5e6c6d73ca2662c=1615595252',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400"}
    res = requests.get(url, headers=headers)
    if res.text.index('1') > 0:
        print("Add cart success")


if __name__ == '__main__':
    add(1, 2)
