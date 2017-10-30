#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-9-10 上午11:42
# @Author  : huiqin
# @File    : MaximumSubarrayList.py
# @Description : Class is for
def FindCross(A, p, r):
    if p == r:
        return (p, r, A[p])
    else:
        mid = (p + r +1) /2
        l_sum, sum_l = - float("inf"), 0
        for i in A[:mid:][::-1]:
            sum_l = sum_l + i
            if sum_l > l_sum:
                l_sum, l_index = sum_l, A.index(i)
        r_sum, sum_r = - float("inf"), 0
        for j in A[mid:]:
            sum_r = sum_r + j
            if sum_r > r_sum:
                r_sum = sum_r
                r_index = A.index(j)

    return (l_index, r_index, l_sum + r_sum)

def FindSubArr(A, p, r):
    if p == r:
        return p, r, A[p]
    else:
        mid = (r + p) /2
        ls_index, le_index , l_sum = FindSubArr(A, p, mid)
        rs_index, re_index , r_sum = FindSubArr(A, mid + 1, r)
        cs_index, ce_index , c_sum = FindCross(A, p, r)
        if l_sum == max([l_sum, r_sum , c_sum ]):
            return ls_index, le_index , l_sum
        elif r_sum == max([l_sum, r_sum , c_sum ]):
            return rs_index, re_index , r_sum
        else:
            return cs_index, ce_index , c_sum

# l = [1, -4, 3, 5, -7, 2, 8, -9]
# l = [1]
# l = [1, -2, 3]
l = [1, -2, 3, 4, 8, -10, 13, 21, -13]

print FindSubArr(l, 0, len(l) -1)