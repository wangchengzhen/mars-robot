import urllib
import re
import os
from urllib.request import urlretrieve

targetDir = r"E:\\Download/"


def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir, path[pos + 1:])
    return t


if __name__ == "__main__":
    url = "http://weapon.huanqiu.com/c_130"
    page = urllib.request.urlopen(url)
    html = page.read()

    # \s:任意空白字符
    # ^：匹配字符串的开头
    # *:匹配前一个字符0次或无数次
    # ?:匹配前一个字符0次或1次


    result = re.findall(r'(http:[^\s]*?(jpg|png|gif))', str(html))

    for link, t in result:
        link = str(link).replace('\\', '');
        print(f'link:{link}')
        url = link.split('/')[-1]

        urlretrieve(link, f'F:/{url}')
    print(f'下载%d张图片' % len(result))