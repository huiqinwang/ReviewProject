#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午2:49
# @Author  : huiqin
# @File    : LongestValidParentheses.py
# @Description : Class is for

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        maxlen = 0
        stack = []
        last = -1
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)     # push the INDEX into the stack!!!!
            else:
                if stack == []:
                    last = i
                else:
                    stack.pop()
                    if stack == []:
                        maxlen = max(maxlen, i-last)
                    else:
                        maxlen = max(maxlen, i-stack[len(stack)-1])
        return maxlen