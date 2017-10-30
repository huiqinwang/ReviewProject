#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-18 下午3:46
# @Author  : huiqin
# @File    : MergeSort.py
# @Description : Class is for

# 归并排序 就是每次合并两个有序表
def merge(left,right):
    '''
    合并两个有序表
    :param left: 
    :param right: 
    :return: 
    '''
    result = []
    i,j = 0,0
    while (i<len(left)) and (j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i = i +1
        else:
            result.append(right[j])
            j = j+1

    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]
    return result

def merge_sort(lists):
    if len(lists) <=1:   #此处一定要小于等于１，只有一个时不用排序返回，不然会一直递归出不来
        return lists
    mid = len(lists)>>1
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    return merge(left,right)



if __name__ == "__main__":
    lists = [9, 3, 8, 7, 3, 4, 5]
    print(merge_sort(lists))