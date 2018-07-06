'''BeautifulSoup库学习'''

from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
'''

soup = BeautifulSoup(html, 'lxml')
# #print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.a)
# print('='*30)
# print(soup.find_all('a'))
# print('='*20)
# print(soup.find(id='link3'))

'''解析器'''
'''BeautifulSoup支持python标准库中的HTML解析器，还支持一些第三方的解析器
，如果没有，则使用python默认的解析器，lxml解析器更加强大，速度更快'''

print(soup.find_all(attrs={'id':'list-1'}))
print('='*30)
print(soup.find_all(attrs={'name':'elements'}))
print('='*30)
print(soup.find_all(text='Foo'))
# find返回匹配到的结果的第一个元素， find_all返回所有匹配到的

for li in soup.select('li'):
    print(li.get_text())

for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 使用lxml解析库
# 尽量使用find 和find_all 查询匹配。也可以使用select 方法