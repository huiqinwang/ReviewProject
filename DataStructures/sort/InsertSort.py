#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-18 上午11:13
# @Author  : huiqin
# @File    : InsertSort.py
# @Description : Class is for

# 直接插入排序，前提：list已经排好序，时间复杂度：O(n^2)
def insert_sort(lists):
    for i in range(len(lists)):
        key = lists[i]
        j = i-1
        while j >= 0:
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            j = j-1
    return lists
if __name__ == "__main__":
    lists = [9,3,8,7,3,4,5]
    print(insert_sort(lists))

