#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-12 下午6:48
# @Author  : huiqin
# @File    : RemoveDuplicates.py
# @Description : Class is for
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                A[i], A[j+1] = A[j+1], A[i]
                j = j + 1
        return j+1


'''
# TT
public class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length <= 2) return nums.length;
        int dup1 = nums[0];
        int dup2 = nums[1];
        int end = 2;
        for(int i = 2; i < nums.length; i++){
            if(nums[i]!=dup1){
                nums[end] = nums[i];
                dup1 = dup2;
                dup2 = nums[i];
                end++;
            }
        }
        return end;
    }
}

'''