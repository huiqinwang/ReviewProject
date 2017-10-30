#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-8 下午4:59
# @Author  : huiqin
# @File    : one.py
# @Description : Class is for
import sys

def binary_search(lists):
    key = 180+lists[0]
    low = 0
    high = len(lists)-1

    while low < high:
        mid = (high+low)>>1
        if lists[mid] > key:
            high = mid - 1
        elif lists[mid] < key and (lists[mid-1] < lists[mid]):
            low = mid +1
        else:
            return mid
    return False


# if __name__ == "__main__":
#     n = int(raw_input()) # 只能获取一行数据，不包括"\n"
#     a = list()
#     for i in range(n):
#         a.append(float(raw_input()))
#
#     mid = len(a)>>2
#     global_max = a[0]
#     for h in range(mid):
#         key = a[h]+180
#         index = h
#         for j in range(h,len(a)):
#             if a[j] > key:
#                 index = j-1
#                 break
#         result = a[index]-a[h]
#         global_max = max(global_max,result)
#
#     print("%.8f"%global_max)


if __name__ == "__main__":
    n = int(raw_input()) # 只能获取一行数据，不包括"\n"
    a = list()
    for i in range(n):
        a.append(float(raw_input()))

    mid = len(a)-1
    for i in range(len(a)):
        if a[i] > (a[0]+180):
            mid = i -1
            break;

    global_max = a[0]
    for h in range(mid):
        key = a[h]+180
        index = len(a)-1
        for j in range(h,len(a)):
            if a[j] > key:
                index = j-1
                break
        result = a[index]-a[h]
        global_max = max(global_max,result)

    print("%.8f"%global_max)