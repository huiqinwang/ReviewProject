#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-14 上午11:25
# @Author  : huiqin
# @File    : InfixToSuffix.py
# @Description : Class is for

#　中缀表达式转化为后缀表达式:9 + ( 3 - 1 ) * 3 + 10 / 2
#  按照三条规则进行判断并相应的行为
def infix_suffix(infix):
    opera_stack = []
    results = []
    symbol = {')':'(','}':'{',']':'['}
    global opera
    opera = {'+': 3, '-': 3, '*': 4, '/': 4}


    def judge_priority(opera1,opera2):
        num1 = opera.get(opera1)
        num2 = opera.get(opera2)
        if num1 <= num2:
            return True
        else:
            return False

    for s in infix:
        if s.isdigit():
            results.append(s)
        elif s in symbol.keys():
            s_value = symbol[s]
            while len(opera_stack)!=0:
                pops = opera_stack.pop()
                results.append(pops)
                if pops == s_value:
                    results.pop()
                    break
        elif s in opera.keys():
            while len(opera_stack)!=0:
                popss = opera_stack.pop()
                if judge_priority(s,popss):
                    results.append(popss)
                else:
                    opera_stack.append(popss)
                    break
            opera_stack.append(s)
        else:
            opera_stack.append(s)
    while len(opera_stack) != 0:
        results.append(opera_stack.pop())
    return ' '.join(results)


if __name__ == "__main__":
    infix = raw_input().strip().split(" ")
    print(infix_suffix(infix=infix))