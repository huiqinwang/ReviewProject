#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午3:39
# @Author  : huiqin
# @File    : one1.py
# @Description : Class is for

import sys

def isUglyNum(num,common_num):
    for i in common_num:
        while num%i==0:
            num = num/i

    if num == 1:
        return True
    else:
        return False
if __name__ == "__main__":
    n = int(raw_input())
    # n = int(sys.stdin.readline().strip())

    count = 1
    num = 1
    ugly_num = 0
    common_num = [2,3,5]
    while count <= n:
        if isUglyNum(num,common_num):
            ugly_num = num
            count +=1
        num += 1
    print(ugly_num)
