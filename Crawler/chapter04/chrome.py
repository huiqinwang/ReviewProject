#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午3:44
# @Author  : huiqin
# @File    : chrome.py
# @Description : Class is for
from urllib import request

url = 'http://blog.csdn.net/weixin_36001351/article/details/72236804'
file = request.urlopen(url)
fhandle1 = open('.chromeCSDN_1.html','wb')
print(file.readlines())
fhandle1.write(file.read())
fhandle1.close()


headers = ('User-Agent',"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
opener = request.build_opener()  #创建自定义opener对象并赋值给opener对象
opener.addheaders = [headers] #opener对象名.addheaders=[头信息]，设置对应头信息
data = opener.open(url).read()  #opener对象open()打开对应网址，read()读取信息到字符串data
hand2 = open('.chromeCSDN2.html','wb')
hand2.write(data)
hand2.close()
print(data)


# 利用request.Request中的add_header()
req = request.Request(url) #创建一个Request对象
# 添加报头信息，格式：Request对象名.add_header(字段名，字段值)
req.add_header('User-Agent',"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
hand3 = open('.chromeCSDN3.html','wb')
data2 = request.urlopen(req).read()
hand3.write(data2)
hand3.close()