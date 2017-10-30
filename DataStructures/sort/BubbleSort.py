#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-18 上午11:20
# @Author  : huiqin
# @File    : BubbleSort.py
# @Description : Class is for

# 冒泡排序
def bubble_sort(lists):
    lens = len(lists)
    for i in range(lens):
        # print(lens-i)
        for j in range(0,(lens-i-1)):
            if lists[j] > lists[j+1]:
                temp = lists[j]
                lists[j] = lists[j+1]
                lists[j+1] = temp
    return lists

if __name__ == "__main__":
    lists = [9,3,8,7,3,4,5]
    print(bubble_sort(lists))