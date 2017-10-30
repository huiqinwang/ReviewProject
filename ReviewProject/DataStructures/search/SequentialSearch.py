#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-27 上午10:59
# @Author  : huiqin
# @File    : SequentialSearch.py
# @Description : Class is for
# 最基础的遍历无序列表的查找算法
# 时间复杂度O(n)

def sequential_search(lists,key):
    for i in range(len(lists)):
        if lists[i] == key:
            return i
    return False

if __name__ == "__main__":
    lists = [1,5,8,123,22,54,7,99,300,222]
    print(sequential_search(lists,54))