'''Selenium'''

'''selenium是一套完整web应用程序测试系统，Selenium的核心Selenium Core基于JsUnit
完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。
'''

'''爬虫中主要用来解决JavaScript渲染问题'''
from selenium import webdriver
# 查看支持的浏览器
#help(webdriver)

'''PhantomJS是一个而基于WebKit的服务端JavaScript API,
支持Web而不需要浏览器支持，其快速、原生支持各种Web标准：Dom处理，
CSS选择器，JSON等等。PhantomJS可以用用于页面自动化、网络监测、网页截屏，
以及无界面测试'''

'''声明浏览器对象'''
# browser = webdriver.Chrome()
# browser = webdriver.Firefox()

'''访问页面,加启动配置'''
# browser = webdriver.ChromeOptions()
# browser.add_argument('disable-infobars')
# '''打开浏览器'''
# drive = webdriver.Chrome(chrome_options=browser)
# drive.get("http://www.baidu.com")  # 此处需要Chrome浏览器的驱动，否则会报错
# print(drive.title)
# drive.close()
# 功能： 打开Chrome浏览器，进入百度页面，然后退出，关闭

# browser = webdriver.Chrome()
# browser.get('http://www.taobao.com')
# input_first = browser.find_element_by_id("q")
# input_second = browser.find_element_by_css_selector("#q")
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)
# browser.close()
#

'''元素交互操作'''
# import time
# browser = webdriver.Chrome()
# browser.get("http://www.taobao.com")
# input_str = browser.find_element_by_id('q')
# input_str.send_keys("ipad")
# time.sleep(1)
# input_str.clear()
# input_str.send_keys("MakBook pro")
# button = browser.find_element_by_class_name('btn-search')
# button.click()

# 我也没有安装驱动器， 写的代码没法测试，没动力。本章不写了
# 详细访问网站：URL = http://www.cnblogs.com/zhaof/p/6953241.html