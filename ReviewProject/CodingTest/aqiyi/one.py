#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午7:27
# @Author  : huiqin
# @File    : one.py
# @Description : Class is for
def nums(s):
    maxlen = 0
    k1 =k2 = 0
    stack = []
    last = -1
    start = end = 0
    if s == '':
        return 0

    for i in range(len(s)):
        if s[i] == '(':
            k1 += 1
            stack.append(i)  # push the INDEX into the stack!!!!
        else:

            if stack == []:
                last = i
            else:
                stack.pop()
                k2 += 1
                if k2 == 1:
                    return  k1
                if stack == []:
                    maxlen = max(maxlen, i - last)
                else:
                    maxlen = max(maxlen, i - stack[len(stack) - 1])
    return maxlen


if __name__ == "__main__":
    s = raw_input()
    s_list = []
    start = 0
    for i in range(len(s)):
        if s[i] == ")":
            s_list.append(i)
    print(s_list)