#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-16 下午6:40
# @Author  : huiqin
# @File    : test1.py
# @Description : Class is for
strs = ['A->B','B->C','C->D','D->B']

strs_map = dict()
strs_set = set()

for str in strs:
    str_split = str.split("->")
    strs_map.setdefault(str_split[0],str_split[1])
    strs_set.add(str_split[0])
    strs_set.add(str_split[1])

result = list()
# for str in strs:
#     str_split = str.split("->")
#     v1 = str_split[0]
#     v2 = str_split[1]
#     temp_map = list()
#     temp_map.append(v1)
#     while v2 in strs_map.keys():
#         if v2 not in temp_map:
#             temp_map.append(v2)
#         else:
#             index = temp_map.index(v2)
#             result.append(temp_map[index:])
#             break
#         temp = strs_map[v2]
#         v2 = temp

str_split = str.split("->")
v1 = str_split[0]
v2 = str_split[1]
temp_map = list()
temp_map.append(v1)
while v2 in strs_map.keys():
    if v2 not in temp_map:
        temp_map.append(v2)
    else:
        index = temp_map.index(v2)
        result=temp_map[index:]
        break
    temp = strs_map[v2]
    v2 = temp

for i in range(len(strs_set)):
    item = list(strs_set)[i]
    if item in result:
        if i != len(strs_set)-1:
            print("{", item, ", ", "true},")
        else:
            print("{", item, ", ", "true}")
    else:
        if i != len(strs_set)-1:
            print("{", item, ", ", "false},")
        else:
            print("{", item, ", ", "false}")


