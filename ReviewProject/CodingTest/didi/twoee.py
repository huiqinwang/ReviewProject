#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午4:28
# @Author  : huiqin
# @File    : twoee.py
# @Description : Class is for
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip("\n"))
    data_list = list()
    data = sys.stdin.readline().strip("\n").split(" ")
    for d in data:
        try:
            data_list.append(int(d))
        except:
            break

    lens = len(data_list)
    result = [[False for i in range(lens)] for j in range(lens)]
    k = 0

    all_result = []
    for i in range(lens):
        if data_list[i] ^ 0 == 0:
            result[i][i] = True
            all_result.append(data_list[i])
            k += 1

    for i in range(lens - 1):
        if (data_list[i] ^ data_list[i + 1] == 0):
            result[i][i + 1] = True
            all_result.append(data_list[i:(i+2)])
            if ((not result[i])):
                k += 1

    for ln in range(3, lens + 1):
        for i in range(0, lens - ln + 1):
            j = i + ln - 1
            if (data_list[i] ^ data_list[j] == 0) and (result[i + 1][j - 1]):
                result[i][j] = True
                all_result.append(data_list[i:j])
                if j-i-1 != 2:
                    k += 1

    print(k)
