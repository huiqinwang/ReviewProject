#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-8 上午11:06
# @Author  : huiqin
# @File    : ClimbStairs.py
# @Description : Class is for

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [1]*(n+1)
        s[0]=s[1]=1
        s[2] = 2

        for i in range(3,n+1):
            temp = (s[i-1]+s[i-2])
            s[i] = temp
        return s[n]

s = Solution()
print(s.climbStairs(5))