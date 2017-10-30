#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-17 下午7:44
# @Author  : huiqin
# @File    : two.py
# @Description : Class is for

if __name__ == "__main__":
    n = int(raw_input())
    input_data = raw_input()
    datas = [int(s) for s in input_data.split(" ")]
    sums = 0
    for item in datas:
        sums += item
    left = 0
    right = n-1

    while left < right:
        if datas[left]==datas[right]:
            left += 1
            right -= 1
        elif datas[left] < datas[right]:
            sums += datas[left]
            left += 1
        else:
            sums += datas[right]
            right -=1

    print(sums)