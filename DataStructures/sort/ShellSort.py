#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-18 上午11:19
# @Author  : huiqin
# @File    : ShellSort.py
# @Description : Class is for

# 希尔排序
def shell_sort(lists,step):
    len_lists = len(lists)
    spike = len_lists/step
    while spike > 0:
        for i in range(0,len_lists,spike):
            key = lists[i]
            j = i -spike
            while j >= 0:
                if lists[j] > key:
                    lists[j+spike] = lists[j]
                    lists[j] = key
                j = j - spike
        spike = spike/step
    return lists

if __name__ == "__main__":
    lists = [9,3,8,7,3,4,5]
    step = 2
    print(shell_sort(lists,step))