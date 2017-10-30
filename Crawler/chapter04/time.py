#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-27 下午4:04
# @Author  : huiqin
# @File    : time.py
# @Description : Class is for
from urllib import request

url ='http://yum.iqianyue.com/yum/index.html'
for i in range(1,100):
    try:
        file = request.urlopen(url,timeout=1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->"+str(e))