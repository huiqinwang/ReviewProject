#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-13 下午7:56
# @Author  : huiqin
# @File    : two.py
# @Description : Class is for
if __name__ == "__main__":
    datas = [2,3,4]

    a_sums =  list()
    b_sums = list()
    a_sums[0] = 0
    a_sums[1] = datas[0]

    b_sums[0] = 0
    b_sums[1] = 0
    count = 1
    i = 2
    while len(datas) != 0:
        if count%2 == 1:
            if a_sums[i-1] > a_sums[i-2]:
                a_sums[i] = a_sums[i-1]

