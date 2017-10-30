#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午4:24
# @Author  : huiqin
# @File    : http.py
# @Description : Class is for
from urllib import request

keyword = 'ggg'
url = 'https://www.baidu.com/s?wd='+keyword
req = request.Request(url)
data = request.urlopen(req).read()
fhand = open('.HTTPKW.html','wb')
fhand.write(data)
fhand.close()


url2 = 'https://www.baidu.com/s?wd='
hanzi = "快乐"
key_code = request.quote(hanzi)
req = request.Request(url2+key_code)
datas = request.urlopen(req).read()
hand = open('.httphanzi.html','wb')
hand.write(datas)
hand.close()

from urllib import request,parse
urls = 'http://www.iqianyue.com/mypost'
# 将数据使用urlencode编码处理后，使用encode()设置为utf-8
postdata = parse.urlencode({"name":'test1','pass':'123456'}).encode('utf-8')
req = request.Request(urls,postdata)
# 一般出现403禁止访问，加header
req.add_header('User-Agent',"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
data2 = request.urlopen(req).read()
hand2 = open('.httppost.html','wb')
hand2.write(data2)
hand2.close()