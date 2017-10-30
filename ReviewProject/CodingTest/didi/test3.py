#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-31 下午8:42
# @Author  : huiqin
# @File    : test3.py
# @Description : Class is for

import numpy as np
class Solution(object):
    def longestPalindrome(self, s,k):
        """
        :type s: str
        :rtype: str
        """
        lens = len(s)
        begin = 0
        max_len = 1
        # result = np.array([False]*(lens*lens)).reshape(lens,lens)
        # # 初始化1:单个字符为回文
        # for i in range(lens):
        #     if result[i][i]%k==0:
        #         result[i][i] = True
        # #初始化2:　相邻字符回文
        # for i in range(lens-1):
        #     tem_sum = s[i]+s[i+1]
        #     if tem_sum%k==0:
        #         result[i][i+1] = True
        #         begin = i
        #         max_len = 2

        # 从len=3开始(3.....len)寻找回文:子问题求解为回文，一直扩大至原问题
        # for ln in range(3,lens+1):
        #     for i in range(0,lens-ln+1):
        #         j = i+ln-1
        #         tem_sum = s[i]+s[j]
        #         if (tem_sum%k==0) and (result[i+1][j-1]):
        #             result[i][j] = True
        #             begin = i
        #             max_len = ln
        # return  s[begin:begin+max_len]
        for ln in range(1,lens+1):
            for i in range(0,lens-ln+1):
                j = i+ln-1
                if i==j and s[i]%k==0:
                    max_len=1
                tem_sum = sum(s[i:j+1])
                if tem_sum%k==0:
                    max_len = ln
        return  max_len


s = Solution()
# lis = [1,2,3,4,5]
# k=5
lis = [5]
k=5
print(s.longestPalindrome(lis,k))