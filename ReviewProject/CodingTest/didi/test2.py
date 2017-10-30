#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-26 下午4:07
# @Author  : huiqin
# @File    : test2.py
# @Description : Class is for

import sys
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right

    while low < high:
        while (low < high) and (lists[high] <= key):
            high = high -1
        lists[low] = lists[high]
        while(low < high) and (lists[low] >= key):
            low = low + 1
        lists[high] = lists[low]
    lists[high] = key
    quick_sort(lists,left,low-1)
    quick_sort(lists,low+1,right)
    return lists

if __name__ == "__main__":
    n = 2
    ans = 0
    line = sys.stdin.readline().strip()
    values = map(int, line.split())
    nums = list(values)

    k = int(sys.stdin.readline().strip())

    # 方案1:用自带的函数
    # nums_sort = sorted(nums,reverse=True)
    # 方案２：用排序算法先排序，快排最适中
    nums_sort = quick_sort(nums,0,len(nums)-1)
    print(nums_sort[k-1])
# 45 67 33 21
