#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 上午10:46
# @Author  : huiqin
# @File    : AutoSmallChangeValue.py
# @Description : Class is for

def giveChange(need_change,currency_list,num_list,used_list):
    for change in range(need_change+1):
        for currency in currency_list:
            tmp = change - currency

            if tmp >= 0 and num_list[tmp]+1 < num_list[change]:
                num_list[change] = num_list[tmp]+1
                used_list[change] = currency
                # used_list.append(currency)

    return

def showChange(need_change,used_list):
    give_list = list()
    while need_change > 0:
        give_list.append(used_list[need_change])
        need_change -= used_list[need_change]
    give_list.sort()
    return  give_list

if __name__ == "__main__":
    need_change = 63
    currency_list = [1,5,10,21,25]
    num_list = list(range(need_change+1))
    used_list = list(range(need_change+1))
    # used_list = list()
    giveChange(need_change,currency_list,num_list,used_list)
    give_list = showChange(need_change,used_list)

    print(("%d need")%(need_change))
    print(give_list)