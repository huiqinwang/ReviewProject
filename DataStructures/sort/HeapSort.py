#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-18 下午3:14
# @Author  : huiqin
# @File    : HeapSort.py
# @Description : Class is for

# 堆排序:一维数组存储完全二叉树
def heap_adjust(lists,i,size):
    lchild = 2*i+1
    rchild = 2*i+2
    max = i
    if i < size/2:
        if (lchild < size) and (lists[lchild] > lists[max]):
            max = lchild
        if (rchild < size) and (lists[rchild] > lists[max]):
            max = rchild
        if max != i:
            lists[i],lists[max] = lists[max],lists[i]
            heap_adjust(lists,max,size)

def heap_build(lists,size):
    '''
    从最下面的父结点开始调整
    :param lists: 
    :param size: 
    :return: 
    '''
    for i in range(size/2)[::-1]:
        heap_adjust(lists,i,size)

def heap_sort(lists):
    size = len(lists)
    heap_build(lists,size)
    for i in range(size)[::-1]:
        lists[0],lists[i] = lists[i],lists[0]
        heap_adjust(lists,0,i)
    return lists

if __name__ == "__main__":
    lists = [9,3,8,7,3,4,5]
    print(heap_sort(lists))