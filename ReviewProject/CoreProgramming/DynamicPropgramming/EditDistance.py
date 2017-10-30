#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-9 上午10:58
# @Author  : huiqin
# @File    : EditDistance.py
# @Description : Class is for
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)+1
        n = len(word2)+1

        res = [[0 for i in range(n)] for j in range(m)]
        for i in range(1,n):
            res[0][i] = i
        for j in range(1,m):
            res[j][0] = j
        for i in range(1,m):
            for j in range(1,n):
                if word1[i-1] == word2[j-1]:
                    res[i][j] = min(res[i-1][j]+1,res[i][j-1]+1,res[i-1][j-1])
                else:
                    res[i][j] = min(res[i-1][j]+1,res[i][j-1]+1,res[i-1][j-1]+1)
        return res[m-1][n-1]

s = Solution()
print(s.minDistance('',''))