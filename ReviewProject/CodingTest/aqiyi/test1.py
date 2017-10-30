#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午8:11
# @Author  : huiqin
# @File    : test1.py
# @Description : Class is for

if __name__ == "__main__":
    s = raw_input()
    count=0
    left = 0
    right = 0
    maxDepth = 0
    for i in range(len(s)):
        if s[i] =="(":
            left += 1
            count += 1
            maxDepth = max(count,maxDepth)
        elif s[i] == ")":
            right += 1
            count -=1
    print(maxDepth)