'''PyQuery 库使用'''

'''网页解析库'''

html= '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
</div>
'''

from pyquery import PyQuery as pq

# doc = pq(html)
# print(doc)
# print(doc('li'))
#
# print('='*10)
# print(doc('#container .list li'))

#doc = pq(html)
#items = doc('.list')
#print(items)


# doc = pq(url="http://www.baidu.com", encoding='utf-8')
# print(doc('head'))

html2 = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
doc = pq(html2)
# print(doc('#container .list li'))
items = doc('.list')
#print(items)
'''查找所有li标签'''
# lis = items.find('li')
# print(lis)
'''通过children和find(li)同样效果'''
# li = items.children()
# print(li)
'''children可以用CSS选择器'''
# li2 = items.children('.active')
# print(li2)

'''parents可以找到父元素内容'''
# container = items.parent()
# print(type(container)) # item只显示到list， parent可以显示到id = container
# print(container)

html3 = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
items_bak = pq(html3)

'''兄弟元素siblings'''
# lst = items_bak('.list .item-0.active')
# print('='*10)
# print(lst.siblings()) # 理论出现的是third time这一档，可是却打印了很多

'''遍历'''
# lis = items_bak('li').items()
# for li in lis:
#     print(type(li))
#     print(li)

'''获取属性'''
# a = items_bak('.item-0.active a')
# print(a)
# print(a.attr('href'))
# print(a.attr.href)

'''获取文本'''
# txt = items_bak('.item-0.active a')
# print(txt)
# print(txt.text())

'''获取HTML'''
# HTML = items_bak('.item-0.active')
# print(HTML)
# print(HTML.html())

'''DOM属性'''
# li = items_bak('.item-0.active')
# print(li)
# li.remove_class('active')
# print(li)
# li.add_class('active')
# print(li)
#
# li.attr('name', 'link') # 熟悉前端可以用后面这两个属性
# print(li)
# li.css('font-size', '14px') # 自定义添加属性内容
# print(li)

'''remove'''
html4 = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
 </div>
'''

doc = pq(html4)
wrap = doc('.wrap')
print(wrap.text()) # Hello, World This is a paragraph
wrap.find('p').remove()
print(wrap.text()) # Hello, World