import urllib
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html.decode('utf-8'))
    for url in imglist:
        print(url)

if __name__ == "__main__":
    html = getHtml("http://tieba.baidu.com/p/2460150866")
    getImg(html)