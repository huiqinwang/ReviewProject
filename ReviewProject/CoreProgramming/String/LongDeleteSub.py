#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-4 下午6:48
# @Author  : huiqin
# @File    : LongDeleteSub.py
# @Description : Class is for
# 字符串删除指定字符

def str_delete(strs,sub):
    hash_list = [0]*256
    for i in sub:
        hash_list[ord(i)]=1

    res = list()
    for s in strs:
        if hash_list[ord(s)] != 1:
            res.append(s)
    return ''.join(res)

if __name__ == "__main__":
    strs = 'They are students'
    sub = 'aeiou'
    print(str_delete(strs,sub))