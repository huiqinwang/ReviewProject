#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午10:36
# @Author  : huiqin
# @File    : urlError.py
# @Description : Class is for
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://www.baidu.com")
except urllib.error.URLError as e: #此处原因为触发了HTTPError，因此可以直接将URLError替换为HTTPError
    print(e.code) # HTTP的代号:403
    print(e.reason) #代号对应的问题：Forbidden


try:
    urllib.request.urlopen("http://www.baidu.com")
except urllib.error.HTTPError as e: #若此处不能处理，即原因不是触发了HTTPError，就用下面的机制处理
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)

try:
    urllib.request.urlopen("http://www.baidu.com")
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)
