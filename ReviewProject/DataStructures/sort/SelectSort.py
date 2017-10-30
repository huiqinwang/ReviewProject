#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-18 下午2:47
# @Author  : huiqin
# @File    : SelectSort.py
# @Description : Class is for

# 直接选择排序
def select_sort(lists):
    for i in range(len(lists)-1):
        min_index = i
        for j in range(i+1,len(lists)):
            if lists[j] < lists[min_index]:
                min_index = j
        lists[i],lists[min_index] = lists[min_index],lists[i]
    return lists

if __name__ == "__main__":
    lists = [9,3,8,7,3,4,5]
    print(select_sort(lists))