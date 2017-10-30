#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午8:03
# @Author  : huiqin
# @File    : two.py
# @Description : Class is for
import sys

def quick_sort(lists, left, right):
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
    n = int(raw_input())
    data_list = list()
    data = sys.stdin.readline().strip("\n").split(" ")
    for d in data:
        try:
            data_list.append(int(d))
        except:
            break
    sort_data = quick_sort(data_list,0,len(data_list)-1)

    sums = 1
    for i in range(len(sort_data)):
        tmp = sort_data[i]
        if tmp - i > 0:
            sums *= (sort_data[i]-i)
            # print sums
    ins = int(10000000007)
    print(sums%ins)
