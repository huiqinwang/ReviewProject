#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 下午2:50
# @Author  : huiqin
# @File    : ValidParentheses.py
# @Description : Class is for
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            if s[i] == ')':
                if stack == [] or stack.pop() != '(':
                    return False
            if s[i] == ']':
                if stack == [] or stack.pop() != '[':
                    return False
            if s[i] == '}':
                if stack == [] or stack.pop() != '{':
                    return False
        if stack:
            return False
        else:
            return True