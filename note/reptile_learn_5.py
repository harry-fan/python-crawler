'''正则表达式'''

import re

# '''
# \w  匹配数字和下划线
# \W  匹配 f 非字母数字下划线
# \s  匹配任意空白字符串
# \S  匹配任意非空字符串
# \d  匹配任意数字
# \D  匹配任意非数字
# \A  匹配字符串开始
# \Z  匹配字符串结束， 存在换行， 只匹配换行前的结束字符串
# \z  匹配字符串结束
# \G  匹配最后匹配完成的位置
# \n  匹配一个换行符
# \t  匹配一个制表符
# ^   匹配字符串的开头
# $   匹配字符串结尾
# .   匹配任意字符
# *   匹配多个
# +   匹配1个或者多个
# {n} 精确匹配n前面的表示
# a | b 匹配a或者b
# ()  匹配括号内的表达式
# '''

# content= "hello 123 4567 World_This is a regex Demo"
# result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}.*Demo$',content)
# print(result)
# print(result.group()) #获取匹配的结果
# print(result.span())  #获取匹配的长度范围
#
# content= "hello 1234567 World_This is a regex Demo"
# result = re.match('^hello\s(\d+)\sWorld.*Demo$',content)
# print(result.group(1))

'''遇见换行进行匹配'''
# content = """hello 123456 world_like
# my name is harry
# """
# result = re.match('^he.*?(\d+).*?harry$', content, re.S)
# print(result)

# content = "price is $5.00"
# result = re.match('price is \$5\.00', content)
# print(result)

# html = '''
# <div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
#         </li>
#     </ul>
# </div>
# '''
# html2 = """
# <div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
#         </li>
#     </ul>
# </div>
# """

# result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
# #print(result)
#
# res = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html2, re.S)
# print(res)

'''实战， 豆瓣扒取图书信息'''
import requests
import re
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102UBrowser/6.1.2107.204 Safari/537.36'
}
content = requests.get("http://book.douban.com",headers).text
#pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
print('enter re.S')
time1 = int(time.time())
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
result = re.findall(pattern, content)
print('get result')


for res in result:
    url,name,author,date=res
    author = re.sub('\s', '', author)
    date = re.sub('\s', '',date)
    print(url, name, author, date)

time2 = int(time.time())
print(time2 - time1)
# 太费时，使用BeautifulSoup库进行查找对应信息，很快。测试了下，re这种耗费90分钟。真特么耗时。