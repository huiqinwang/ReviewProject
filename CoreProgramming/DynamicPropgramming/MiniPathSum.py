#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-9 上午10:17
# @Author  : huiqin
# @File    : MiniPathSum.py
# @Description : Class is for
from copy import deepcopy

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        res = deepcopy(grid)
        for i in range(1,n):res[0][i] += res[0][i-1]
        for j in range(1,m):res[j][0] += res[j-1][0]
        for i in range(1,m):
            for j in range(1,n):
                res[i][j] = min(res[i-1][j],res[i][j-1])+res[i][j]
        return res[m-1][n-1]



s = Solution()
print(s.minPathSum([[1]]))