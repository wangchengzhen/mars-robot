#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import re
from db.db import *
import time
from bs4 import BeautifulSoup
import _thread


def removeComma(word):
    return int(word.replace(',', ''))


def extractNumber(word):
    return word.split(' ')[0]


def insertInfo(articleId):
	print(f'articleId:{articleId}')
	try:
		page = urllib.request.urlopen(f'https://www.zhihu.com/question/{articleId}')
		html = page.read()
		soup = BeautifulSoup(html, 'html.parser', from_encoding='UTF-8')
		follow = soup.select('.NumberBoard-itemValue')[0].get_text()
		pv = soup.select('.NumberBoard-itemValue')[1].get_text()
		title = soup.select('.QuestionHeader-title')[0].get_text()
		content = soup.select('span.RichText.ztext')[0].get_text()
		answer = soup.select('.List-headerText > span')[0].get_text()
		answer = removeComma(extractNumber(answer))
		follow = removeComma(follow)
		pv = removeComma(pv)
		if answer > 200:
			sql = "insert into t_article (id, title, content, answer, follow, pv) values " \
				  "(%d,'%s','%s',%d, %d, %d)" % (articleId, title, content, answer, follow, pv)
			print(sql)
			insert(sql)

	except:
		print("id:%d,error" % articleId)

def printInfo():
	print("ok")

if __name__ == "__main__":
	for i in range(407742265, 407742275):
		insertInfo(i)

