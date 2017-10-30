#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-15 上午11:34
# @Author  : huiqin
# @File    : Preorder.py
# @Description : Class is for

from Tree import Tree

def recursion_pre(root,result):
    '''
    递归前序遍历树
    :param node: 
    :return: 
    '''
    if not root:
        return None
    result.append(root.val)
    recursion_pre(root.lchild,result)
    recursion_pre(root.rchild,result)

def stack_pre(root,result):
    '''
    栈实现非递归前序遍历树，根据正常前序遍历顺序
    :param node: 
    :return: 
    '''
    pre_stack = []
    node = root
    while node or pre_stack:   #也能用while pre_stack判断栈是否存
        while node: #深度遍历,每个结点都先遍历自己，然后遍历左子树，最后遍历右子树
            result.append(node.val)
            pre_stack.append(node) #根结点
            node = node.lchild #左结点（前序遍历一直深入），直到左子树到最左
        node = pre_stack.pop() #实现后退
        node = node.rchild #后退过程，访问右子树

def queue_pre(root,result):
    '''
    利用队列实现非递归遍历树 貌似不合适
    :param root: 
    :param result: 
    :return: 
    '''
    pass


if __name__ == "__main__":
    tree = Tree()
    root = tree.get_tree_root()
    # pre_result = []
    # recursion_pre(root,pre_result) #引用传递
    # print(pre_result)
    pre_stack_result = []
    stack_pre(root,pre_stack_result)
    print(pre_stack_result)



