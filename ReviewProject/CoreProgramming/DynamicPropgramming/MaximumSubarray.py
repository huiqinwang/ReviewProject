#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 上午11:39
# @Author  : huiqin
# @File    : MaximumSubarray.py
# @Description : Class is for
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        globals = locals = nums[0]
        for i in range(1,len(nums)):
            globals = max(nums[i],globals+nums[i])
            locals = max(locals,globals)
        return locals