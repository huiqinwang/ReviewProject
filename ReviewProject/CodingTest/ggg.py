#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-14 下午8:52
# @Author  : huiqin
# @File    : ggg.py
# @Description : Class is for
if __name__ == "__main__":
    n = int(raw_input())
    data_str = raw_input().split(" ")
    data_num = [int(tmp) for tmp in data_str]

    if data_num[n-1] == 1:
        print("Alice")
    else:
        print('Bob')