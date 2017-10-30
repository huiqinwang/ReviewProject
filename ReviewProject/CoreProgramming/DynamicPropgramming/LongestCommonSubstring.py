#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-17 下午6:31
# @Author  : huiqin
# @File    : LongestCommonSubstring.py
# @Description : Class is for

def find_longestStr(s1,s2):
    dp = [[0 for i in range(len(s1)+1)] for j in range(len(s2)+1)]
    max_len = 0
    start = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j]+1
                if dp[i+1][j+1] > max_len:
                    max_len = dp[i+1][j+1]
                    start = i+1
    return s1[start-max_len:start]

if __name__ == "__main__":
    s1 = 'abcdfd'
    s2 = 'accdrg'
    print(find_longestStr(s1,s2))