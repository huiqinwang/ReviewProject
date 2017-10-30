#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-15 下午2:57
# @Author  : huiqin
# @File    : Node.py
# @Description : Class is for
class Node:

    def __init__(self,val="#"):
        self.val = val
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return self.val+"->lchild "+self.lchild.val+"->rchild "+self.rchild.val