#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午8:54
# @Author  : huiqin
# @File    : ss.py
# @Description : Class is for

if __name__ == "__main__":
    s = raw_input()
    sums = 0
    maxs = 0
    arr = 0
    for i in range(len(s)-2):
        print(i)
        arr[i] = s[i:(i+1)]

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                f = j
                max_len = min(f,len(arr))
                for m in range(i+1,max_len):
                    if arr[m] == arr[j]:
                        sums +=1
                    f += 1
                    max_len = min(f,len(arr))
                if maxs < sums:
                    maxs = sums
    print(max)