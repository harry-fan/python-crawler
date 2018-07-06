import urllib.request

response = urllib.request.urlopen('http://www.baidu.com') #urlopem(url, data, timeout)
response.read().decode('utf-8')

'''data 参数的使用例子'''
import urllib.parse

data = bytes(urllib.parse.urlencode({'world':'harry'}), encoding='utf-8')
#print(data)
response = urllib.request.urlopen('http://www.baidu.com', data=data)
response.read()

'''timeout'''
response = urllib.request.urlopen('http://www.baidu.com', timeout=5)
response.read()

'''异常'''
import socket
import urllib.error

try:
    response = urllib.request.urlopen('http://www.baidu.com', timeout=1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('time out', e)

'''set headers'''
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102UBrowser/6.1.2107.204 Safari/537.36',
    'Host':'www.baidu.com'
}
harry = {'boy':'harry'}
data = bytes(urllib.parse.urlencode(harry), encoding='utf-8')
req = urllib.request.Request('http://www.baidu.com', harry, headers, method='POST')
#headers 也可以用方法 req.add_header('User-Agent':'...')
response = urllib.request.urlopen(req)
response.read().decode('utf-8')

'''使用代理访问'''

proxy = urllib.request.ProxyHandler({
    'http':'http://127.0.0.1:9527',
    'http':'https://127.0.0.1:9527'
})

build_opener = urllib.request.build_opener(proxy)
response = build_opener.open('http://www.baidu.com')
print(response.read())

'''cookie使用'''
import http.cookiejar

cookie = http.cookiejar.CookieJar()
hander = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(hander)
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name + '=' + item.value)