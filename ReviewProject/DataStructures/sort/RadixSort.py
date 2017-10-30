#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-18 下午4:01
# @Author  : huiqin
# @File    : RadixSort.py
# @Description : Class is for


#基数排序
import math
def radix_sort(lists, radix=10):
    k = int(math.ceil(math.log(max(lists), radix)))
    print(k)
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):#根据位数多少，循环多少次（每次比较一个位数：个位、十位。。。）
        for j in lists:
            # print(j/(radix**(i-1)) % (radix**i)) #求个位数数字（10个桶）
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
            print(i,j,bucket)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists

if __name__ == "__main__":
    lists = [9,93,3, 8, 7, 3, 4, 5]
    print(radix_sort(lists))