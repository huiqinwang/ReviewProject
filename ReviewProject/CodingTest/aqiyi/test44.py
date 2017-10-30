#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午8:36
# @Author  : huiqin
# @File    : test44.py
# @Description : Class is for
def min(s):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    max_len = 0
    lens = len(s)
    for i in range(lens):
        tmp = s[i]
        flag = False
        for j in range(i+1,lens):
           if tmp == s[j]:
               # print(tmp, s[i])
               flag = True
        if flag:
            # print(max_len)
            max_len += 1
    return max_len*2

if __name__ == "__main__":
    s = raw_input()
    print(min(s))
