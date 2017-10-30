#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-8 下午3:52
# @Author  : huiqin
# @File    : UniquePath.py
# @Description : Class is for
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = list()
        if m == 1 and n == 1:
            paths = [[1]]
        elif m == 1:
            paths = [[1 for i in range(n)]]
        elif n == 1:
            paths = [[1] for i in range(m)]
        else:
            paths = [[0 for i in range(n)] for j in range(m)]
            for h in range(n):
                paths[0][h] = 1
            for j in range(m):
                paths[j][0] = 1
            for i in range(1,m):
                for j in range(1,n):
                    paths[i][j] = paths[i-1][j]+paths[i][j-1]
        print(paths)
        return paths[m-1][n-1]


s = Solution()
print(s.uniquePaths(1,2))
