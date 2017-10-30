#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 上午10:35
# @Author  : huiqin
# @File    : AutoSmallChange.py
# @Description : Class is for

def giveChange(need_change,currency_list,num_list):
    for change in range(need_change+1):
        for currency in currency_list:
            tmp = change - currency

            if tmp >= 0 and num_list[tmp]+1 < num_list[change]:
                num_list[change] = num_list[tmp]+1
    return

if __name__ == "__main__":
    need_change = 63
    currency_list = [1,5,10,21,25]
    num_list = list(range(need_change+1))
    giveChange(need_change,currency_list,num_list)

    print(("%d need %d ")%(need_change,num_list[need_change]))