#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-9 下午1:58
# @Author  : huiqin
# @File    : MaximunSubarray.py
# @Description : Class is for
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p_max = nums[0]
        n_min = nums[0]
        global_max = nums[0]
        for i in range(1,len(nums)):
            tmp = nums[i]
            if tmp > 0:
                p_max = max(p_max*tmp,tmp)
                n_min = n_min*tmp
            elif tmp < 0:
                p_max = n_min*tmp
                n_min = min(p_max*tmp,tmp)
            global_max = max(p_max,global_max)
        return global_max

s = Solution()
print(s.maxProduct([-2,3,-4]))