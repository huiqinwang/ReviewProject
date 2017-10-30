#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-9 下午4:06
# @Author  : huiqin
# @File    : test1.py
# @Description : Class is for

if __name__ == "__main__":
    n = int(raw_input())
    lens_list = list()
    data_list = list()
    for i in range(n):
        tmp_list = list()
        lens_list.append(int(raw_input()))
        tmp_input = list(int(x) for x in raw_input().split(" "))
        data_list.append(tmp_input)
    # print(data_list)

    for tmp_data in data_list:
        # print tmp_data

        lens_ok = 0
        for tmp in  tmp_data:
            if tmp%4 == 0:
                lens_ok += 1
        # print(lens_ok)

        tmp_len = len(tmp_data)
        if tmp_len%2 == 0:
            if lens_ok*2 >= tmp_len:
                print("Yes")
            else:
                print("No")
        elif lens_ok*2+1 >= tmp_len:
            print("Yes")
        else:
            print("No")

