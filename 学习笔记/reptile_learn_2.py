'''
cookie可以写入到文件中保存，有两种方式http.cookiejar.MozillaCookieJar和http.cookiejar.LWPCookieJar()
'''
import http.cookiejar, urllib.request

'''http.cookiejar.MozillaCookieJar()方式'''
# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handle = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handle)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

'''http.cookiejar.LWPCookieJar()方式'''
# filename = 'cook.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handle = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handle)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_expires=True, ignore_discard=True)

'''通过获取文件中的cookie获取的话可以通过load方式，当然用哪种方式写入的，就用哪种方式读取'''
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cook.txt', ignore_discard=True, ignore_expires=True)
handle = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handle)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))