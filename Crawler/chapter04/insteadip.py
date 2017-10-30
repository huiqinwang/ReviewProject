#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午4:55
# @Author  : huiqin
# @File    : insteadip.py
# @Description : Class is for
def use_proxy(proxy_addr,url):
    import urllib.request
    proxy = urllib.request.ProxyHandler({'http':proxy_addr}) #设置对应的代理服务器的地址
    req = urllib.request.build_opener(proxy_addr,urllib.request.HTTPHandler) #自定义opener对象
    urllib.request.install_opener(req) #创建全局默认的opener对象，便于后面urlopen(url)时使用安装的opener对象
    data = urllib.request.urlopen(url).read().decode('utf-8')
    return data

proxy_addr = '202.75.210.45:7777'
data = use_proxy(proxy_addr)
print(len(data))


import urllib.request
url = 'www.baidu.com'
httphd =urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()