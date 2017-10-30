#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午3:08
# @Author  : huiqin
# @File    : urlopen.py
# @Description : Class is for
from urllib import request

file = request.urlopen("http://www.baidu.com")
data = file.readline()
print(data)
fhandle = open(".baidu.html",'wb')
fhandle.write(file.read())
request.urlretrieve("http://www.baidu.com",filename='.baidu2.html')