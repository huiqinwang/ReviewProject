#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-12 下午6:41
# @Author  : huiqin
# @File    : 3SumClosest.py
# @Description : Class is for
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        MIN = pow(2, 31)
        if nums == None:
            return []
        nums.sort()

        lens = len(nums)
        if len < 3:
            return []

        for i in range(0, lens - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = lens - 1

            while left < right:
                sub_sum = nums[left] + nums[right] + nums[i]

                if abs(sub_sum - target) < abs(MIN):
                    MIN = sub_sum - target

                if sub_sum == target:
                    return sub_sum
                elif sub_sum > target:
                    right -= 1
                else:
                    left += 1

        return MIN + target