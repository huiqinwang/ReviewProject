#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-15 上午11:39
# @Author  : huiqin
# @File    : Levelorder.py
# @Description : Class is for
from Tree import Tree

def queue_level(root,result):
    '''
    队列实现层序遍历二叉树
    :param root: 
    :param result: 
    :return: 
    '''
    leval_queue = []
    leval_queue.append(root)
    while leval_queue:
        node = leval_queue.pop(0)
        result.append(node.val)
        if node.lchild:
            leval_queue.append(node.lchild)
        if node.rchild:
            leval_queue.append(node.rchild)


if __name__ == "__main__":
    tree = Tree()
    root = tree.get_tree_root()
    result_queue_level = []
    queue_level(root,result_queue_level)
    print(result_queue_level)
