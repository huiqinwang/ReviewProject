#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-13 下午4:23
# @Author  : huiqin
# @File    : test.py
# @Description : Class is for

if __name__ == "__main__":
    s = raw_input()
    datas = [int(x) for x in s.split(" ")]
    print(datas)

    result = list()
    a,b,c,d = datas[0],datas[1],datas[2],datas[3]
    while c!=a and d!=b:
        if c % 2 == 0 and d % 2 == 0:
            result.append("2")
        elif c - 1 != 0 and d - 1 != 0:
            result.append("1")
    print(len(result))