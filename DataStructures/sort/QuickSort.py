#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-18 下午2:10
# @Author  : huiqin
# @File    : QuickSort.py
# @Description : Class is for

# 快速排序
def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right

    while low < high:
        while (low < high) and (lists[high] >= key):
            high = high -1
        lists[low] = lists[high]
        while(low < high) and (lists[low] <= key):
            low = low + 1
        lists[high] = lists[low]
    lists[high] = key
    quick_sort(lists,left,low-1)
    quick_sort(lists,low+1,right)
    return lists


if __name__ == "__main__":
    lists = [9,3,8,7,3,4,5]
    print(quick_sort(lists,0,len(lists)-1))




