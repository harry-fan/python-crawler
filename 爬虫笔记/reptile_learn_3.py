''''''
from urllib import request, error

'''异常处理'''
# try:
#     response = request.urlopen("http://pythonsite.com/1111.html")
# except error.URLError as e:
#     print(e.reason)

'''上面是URLError错误, 还有HTTPError错误, 后者包含三个属性, code, reason, headers'''
# try:
#     response = request.urlopen("http://pythonsite.com/1111.html")
# except error.HTTPError as e:
#     print('enter HTTPError')
#     print(e.reason)
#     print('='*30)
#     print(e.code)
#     print('=' * 30)
#     print(e.headers)
# except error.URLError as e:
#     print("enter URLError")
#     print(e.reason)
# else:
#     print("request successfully")

'''URL解析'''
# from urllib.parse import urlparse
# from urllib.parse import urlunparse
#
# result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# print("result = ", result)
#
# data = ['http', 'www.baidu.com', 'index.html','user','a=123','commit']
# print(urlunparse(data))

'''urljoin 拼接'''
# from urllib.parse import urljoin
#
# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
# print(urljoin('http://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'))
# print(urljoin('https://pythonsite.com/FAQ.html', 'http://www.baidu.com'))
#后面的URL会覆盖掉前面的（完整的拼接），即同样完整的URL后面优先级高

'''urlencode字典转换URL参数'''
from urllib.parse import urlencode

params = {"name":"harry", "age":24,}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)