#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-13 下午8:04
# @Author  : huiqin
# @File    : test.py
# @Description : Class is for

def test(a):
    # a = a+1
    a.pop()
    return a

if __name__ == "__main__":
    # a = 1
    a = [1,2,3]
    test(a)
    print(a)