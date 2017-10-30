#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-17 下午7:24
# @Author  : huiqin
# @File    : one.py
# @Description : Class is for

def judge_path(path):
    path_split = path.split("/")
    stacks = list()
    simbal = ["", ".", "..", "/"]
    res = ""
    for tmp in path_split:
        if tmp not in simbal:
            stacks.append(tmp)
        if ".." == tmp and stacks:
            stacks.pop()
    if len(stacks) == 0:
        return "/"
    for item in stacks:
        res += "/" + item + ""
    return res

if __name__ == "__main__":
    path = raw_input()
    print(judge_path(path))
# /a/./b/../../c/