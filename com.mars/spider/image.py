import re
import time
from urllib.request import urlopen, urlretrieve


# 下载HTML
def getHtml(url):
    page = urlopen(url)
    html = page.read()
    return html


# 从html中解析出图片URL
def getImg(html):
    reg = r'src="(.*?\.jpg)"'
    patternImage = re.compile(reg)
    told = html.decode('utf-8')
    images = patternImage.findall(told)
    return images


# 下载处理
def imgDownload(imgUrl):
    urlretrieve(imgUrl, '%s.jpg' % time.time())


# 主函数
def main():
    url = 'https://www.maigoo.com/tuku/430107.html'
    html = getHtml(url)
    print(html)
    imgList = getImg(html)
    for imgUrl in imgList:
        print(imgUrl)
        imgDownload(imgUrl)


# 执行主函数
if __name__ == '__main__':
    main()
