#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-15 上午11:38
# @Author  : huiqin
# @File    : Inorder.py
# @Description : Class is for
from Tree import Tree

def recursion_in(root,result):
    '''
    按中序遍历顺序访问树，并保存
    :param root: 
    :param result: 
    :return: 
    '''
    if not root:
        return 0
    recursion_in(root.lchild,result)
    result.append(root.val)
    recursion_in(root.rchild,result)

def stack_in(root,result):
    '''
    栈实现非递归遍历二叉树
    :param root: 
    :param result: 
    :return: 
    '''
    in_stack = []
    node = root
    while node or in_stack:
        while node:
            in_stack.append(node)
            node = node.lchild
        node = in_stack.pop()
        result.append(node.val)
        node = node.rchild


if __name__ == "__main__":
    tree = Tree()
    root = tree.get_tree_root()
    result_in = []
    recursion_in(root,result_in)
    print result_in
    result_stack_in = []
    stack_in(root,result_stack_in)
    print(result_stack_in)

