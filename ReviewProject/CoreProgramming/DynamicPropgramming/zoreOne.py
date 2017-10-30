#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-12 下午3:48
# @Author  : huiqin
# @File    : zoreOne.py
# @Description : Class is for

import numpy as np
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        begin = 0
        max_len = 1
        result = np.array([False]*(lens*lens)).reshape(lens,lens)
        # 初始化1:单个字符为回文
        for i in range(lens):
            result[i][i] = True
        #初始化2:　相邻字符回文
        for i in range(lens-1):
            if s[i] != s[i+1]:
                result[i][i+1] = True
                begin = i
                max_len = 2

        # 从len=3开始(3.....len)寻找回文:子问题求解为回文，一直扩大至原问题
        for ln in range(3,lens+1):
            for i in range(0,lens-ln+1):
                j = i+ln-1
                if ln%2 == 1:
                    if (s[i] == s[j]) and (result[i + 1][j - 1])and (s[i+1] != s[i]):
                        result[i][j] = True
                        begin = i
                        max_len = ln
                else:
                    if (s[i] != s[j]) and (result[i + 1][j - 1]) and (s[i+1] != s[i]):
                        result[i][j] = True
                        begin = i
                        max_len = ln

        print(max_len)
        return  s[begin:begin+max_len]

s = Solution()
print(s.longestPalindrome('11111111010101011'))