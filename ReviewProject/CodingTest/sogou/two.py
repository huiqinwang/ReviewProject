#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-8 下午5:38
# @Author  : huiqin
# @File    : two.py
# @Description : Class is for
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
            if s[i] == s[i+1]:
                result[i][i+1] = True
                begin = i
                max_len = 2

        # 从len=3开始(3.....len)寻找回文:子问题求解为回文，一直扩大至原问题
        for ln in range(3,lens+1):
            for i in range(0,lens-ln+1):
                j = i+ln-1
                if (s[i] == s[j]) and (result[i+1][j-1]):
                    result[i][j] = True
                    begin = i
                    max_len = ln
        return  s[begin:begin+max_len]

if __name__ == "__main__":
    n = int(raw_input()) # 只能获取一行数据，不包括"\n"
    a = list()
    for i in range(n):
        a.append(float(raw_input()))

    global_max = a[0]
    for h in range(len(a)):
        key = a[h]+180
        index = h
        for j in range(h,len(a)):
            if a[j] > key:
                index = j-1
                break
        result = a[index]-a[h]
        global_max = max(global_max,result)

    print("%.8f"%global_max)