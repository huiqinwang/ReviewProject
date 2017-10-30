#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-12 下午6:20
# @Author  : huiqin
# @File    : ValidParenthese.py
# @Description : Class is for

class Solution(object):
    def isValid(self,s):

        def isMatch(l,r):
            return ('('==l and ')'==r) or ('['==l and ']'==r) or ('{'==l and '}'==r)

        stacks = []
        if len(s) == 0:
            return False
        for c in s:
            if len(stacks) == 0 or not isMatch(stacks[-1],c):
                stacks.append(c)
            else:
                stacks.pop()
        return len(stacks)==0

