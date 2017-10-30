#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-14 下午8:29
# @Author  : huiqin
# @File    : meituan.py
# @Description : Class is for

def isRight(data_str,lens):
    lens = len(data_str)
    count = 0
    if lens == 0:
        return 0
    if lens == 1 :
        if int(data_str[0])%7 == 0:
            return 1
        else:
            return 0

    for i in range(lens):
        for j in range(i+1,lens):
            tmp = data_str[i] + data_str[j]
            tmp2 = data_str[j] + data_str[i]
            # print(tmp)
            if int(tmp) % 7 == 0:
                count += 1
            if int(tmp2) % 7 == 0:
                count += 1
    return count

if __name__ == "__main__":
    n = int(raw_input())
    data_str = raw_input().split(" ")
    lens = len(data_str)
    print(isRight(data_str,lens))