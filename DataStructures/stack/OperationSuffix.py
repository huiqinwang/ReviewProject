#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-14 上午10:36
# @Author  : huiqin
# @File    : OperationSuffix.py
# @Description : Class is for

# 后缀表达式计算: 9 3 1 - 3 * + 10 2 / +
def operate_suffix(suffix):
    num_stack = []
    for s in suffix:
        # print num_stack
        if s.isdigit():
            num_stack.append(s)
        elif len(num_stack) >= 2:
            num1 = num_stack.pop()
            num2 = num_stack.pop()
            # print('%s %s %s')%(num2,s,num1)
            reprs = num2+s+num1
            results = eval(reprs)
            num_stack.append(str(results))
    return num_stack.pop()

if __name__ == "__main__":
    suffix = raw_input().strip().split(" ")
    print operate_suffix(suffix=suffix)
