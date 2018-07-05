# coding:utf-8
import urllib.request#python3很多模块需要这样导入
import re

def getHtmlContent(url):
    page = urllib.request.urlopen(url)
    return page.read()

def getJPGs(html):
    jpgsRrg = re.compile(r'<img.+?src="(.+?\.jpg)" width')#正则
    print(jpgsRrg)
    jpgs = re.findall(jpgsRrg, html)
    return jpgs

#用图片url下载图片并保存成制定文件名
def download(imgurl, filename):
    urllib.request.urlretrieve(imgurl, filename)

#批量下载
def batchDownload(imgUrls, path='./'):
    count = 1
    #print(imgUrls)
    for url in imgUrls:
        download(url, ''.join([path, '{0}.jpg'.format(count)]))
        print("已爬取第%s张" % count)
        count = count + 1

def downloadStart(url):
    html = getHtmlContent(url)
    html=html.decode('utf-8')
    jpgs = getJPGs(html)
    batchDownload(jpgs)

def main():
    url = 'http://tieba.baidu.com/p/2256306796'
    downloadStart(url)

if __name__ == '__main__':
    main()