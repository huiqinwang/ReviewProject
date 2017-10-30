#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午4:10
# @Author  : huiqin
# @File    : two.py
# @Description : Class is for

def isXOR(num_list):


if __name__ == "__main__":
    n = int(raw_input())
    data_list = [int(x) for x in raw_input().split(" ")]

    lens = len(data_list)
    result = [[False for i in range(lens)] for j in range(lens)]

    k = 0
    for i in range(lens):
        if data_list[i]^0 == 0:
            result[i][i] = True
            k += 1
    for i in range(lens - 1):
        if data_list[i]^ data_list[i + 1]==0:
            result[i][i + 1] = True
            k += 1

    # 从len=3开始(3.....len)寻找回文:子问题求解为回文，一直扩大至原问题
    for ln in range(3, lens + 1):
        for i in range(0, lens - ln + 1):
            j = i + ln - 1
            if (data_list[i]^data_list[j]==0) and (result[i + 1][j - 1]):
                result[i][j] = True
                k += 1
    print(k)

    k = 0
    for n in range(1,lens):
        for i in range(lens):
            j = i+n
            tmp_data = data_list[i,j]
            if j == 0:
                if tmp_data ^ 0 == 0:
                    k += 1
            else:
                if isXOR()



    print(data_list)