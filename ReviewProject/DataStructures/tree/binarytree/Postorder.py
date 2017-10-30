#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-15 上午11:39
# @Author  : huiqin
# @File    : Postorder.py
# @Description : Class is for
from Tree import Tree
def recursion_post(root,result):
    '''
    递归实现手后序遍历树，按照左子树，根结点，右子树顺序
    :param root: 
    :param result: 
    :return: 
    '''
    if not root:
        return 0
    recursion_post(root.lchild,result)
    recursion_post(root.rchild,result)
    result.append(root.val)

def stack_post(root,result):
    '''
    栈实现非递归遍历二叉树，利用两个栈实现
    :param root: 
    :param result: 
    :return: 
    '''
    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:                      #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
        node = stack1.pop()
        if node.lchild:
            stack1.append(node.lchild)
        if node.rchild:
            stack1.append(node.rchild)
        stack2.append(node) #将stack2中的元素出栈，即为后序遍历次序:右子树、左子树、根
    while stack2:
        result.append(stack2.pop().val)



if __name__ == "__main__":
    tree = Tree()
    root = tree.get_tree_root()
    result_post = []
    recursion_post(root,result_post)
    print(result_post)
    result_stack_post = []
    stack_post(root,result_stack_post)
    print(result_stack_post)