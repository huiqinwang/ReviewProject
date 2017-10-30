#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-8 下午5:40
# @Author  : huiqin
# @File    : three.py
# @Description : Class is for

if __name__ == "__main__":
    n = int(raw_input()) # 只能获取一行数据，不包括"\n"
    a = list()
    for i in range(n):
        a.append(float(raw_input()))
    if n == 1:
        print("%.8f"%a[0])

    mid = len(a)>>2
    global_max = a[0]
    for h in range(mid):
        key = a[h]+180
        flag = False
        for j in range(h,len(a)):
            if a[j] > key:
                index = j-1
                flag = True
                break
        if not flag:
            index = len(a)-1

        result = a[index]-a[h]
        global_max = max(global_max,result)

    print("%.8f"%global_max)
