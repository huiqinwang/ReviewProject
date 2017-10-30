#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-27 上午11:03
# @Author  : huiqin
# @File    : BinarySearch.py
# @Description : Class is for

# 针对有序查找表的二分查找算法
# 时间复杂度O(log(n))
def binary_search(lists,key):
    low = 0
    high = len(lists)-1

    while low < high:
        mid = (high+low)>>1
        if lists[mid] > key:
            high = mid - 1
        elif lists[mid] < key:
            low = mid +1
        else:
            return mid
    return False

if __name__ == "__main__":
    lists = [1,5,8,123,22,54,7,99,300,222]
    print(binary_search(lists,54))