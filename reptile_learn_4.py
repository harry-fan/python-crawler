
'''Request库基本使用'''
import requests
'''requests是python实现的最简单易用的HTTP库，建议爬虫使用requests库'''
# response = requests.get("https://www.baidu.com")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# #print(response.text)
# print(response.cookies)
# print(response.content)
# print('='*100)
# print(response.content.decode("utf-8")) #使用decode('utf-8')避免乱码生成

'''
decode():是解码
encode()是编码
'''
#response = requests.get("http://www.baidu.com")
#response.encoding = 'utf-8' # 避免乱码
#print(response.text)

'''不同的请求方式'''
url = "http://www.baidu.com"
# requests.post(url=url,data=None,json=None)
# requests.put(url=url,data=None)
# requests.delete(url)
# requests.head(url)
# requests.options(url)

'''基本请求 get'''
# response = requests.get(url)
# print(response)

'''Requests模块允许使用params关键字传递参数'''
# data = {
#     "name":"harry",
#     "age":"24",
# }
# response = requests.get("url", params=data)
# response.url
# response.text

# import json
# response = requests.get("http://httpbin.org/get")
# print(type(response.text))
#print(type(response.json()))
#print(json.loads(response.text))

'''添加headers'''
# 如果不添加headers，部分网站是不能进行访问的
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102UBrowser/6.1.2107.204 Safari/537.36"
# }
# response = requests.get("https://www.zhihu.com", headers)
# print(response.text)

'''post 请求可以携带参数'''

'''会话维持,cookie作用模拟登陆，做会话维持'''
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456")
# response = s.get("http://httpbin.org/cookies")
# print(response.text)

'''HTTPS会进行证书验证'''
#response = requests.get("https://www.12306.cn")
#print(response.status_code) #证书错误，该网站不是私密链接

import urllib3
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

'''代理设置'''
proxies = {
    "http":"http://127.0.0.1:9999",
    "https":"http://127.0.0.1:8888"
}
response = requests.get("http://www.baidu.com", proxies=proxies)

