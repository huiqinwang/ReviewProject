#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午8:21
# @Author  : huiqin
# @File    : test33.py
# @Description : Class is for

if __name__ == "__main__":
    s = raw_input()
    count=0
    left = 0
    right = 0
    maxDepth = 0
    sums = 0
    maxs = 0
    tmp = list()
    for i in range(len(s)-1):
        tmp[i] = s[i:i+1]
        if tmp[i] == "(":
            sums += 1
        else:
            sums -=1
        maxs = max(sums,maxs)