#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-17 上午9:44
# @Author  : huiqin
# @File    : Haffman.py
# @Description : Class is for


class Node:
    def __init__(self,val=-1):
        self.val = val
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return str(self.val)

def create_tree():
    '''
    构建一系列结点，结点还没有关系
    :return: 
    '''
    list_node = []
    n = int(raw_input("please input the node's number:\n").strip())
    for i in range(n):
        val = int(raw_input("node's value:\n").strip())
        node = Node(val)
        list_node.append(node)
    return list_node


def sort_node(list_node):
    '''
    自定义sort比较函数，比较内容时val
    :param list: 
    :return: 
    '''
    sort_list = sorted(list_node,key=lambda node:node.val)
    return sort_list

def create_Haffman(list_node):
    '''
    构造Haffman树
    :param list: 
    :return: 
    '''
    while len(list_node) !=1 :
        list_node = sort_node(list_node)
        lchild = list_node.pop(0)
        rchild = list_node.pop(0)
        # print("lchild:%s rchild:%s")%(lchild.val,rchild.val)
        new = Node()
        new.val = lchild.val + rchild.val
        new.lchild = lchild
        new.rchild = rchild
        list_node.append(new)
        print("lchild:%s node:%s rchild:%s") % (new.lchild.val, new.val, new.rchild.val)
    return list_node.pop(0)

def recursion_in(root,results):
    '''
    递归中序遍历二叉树
    :param root: 
    :param results: 
    :return: 
    '''
    if not root:
        return 0
    recursion_in(root.lchild,results)
    results.append(root.val)
    recursion_in(root.rchild,results)

def recursion_pre(root,results):
    '''
    递归前序遍历二叉树
    :param root: 
    :param results: 
    :return: 
    '''
    if not root:
        return 0
    results.append(root.val)
    recursion_in(root.lchild,results)
    recursion_in(root.rchild,results)

def get_depth(root):
    '''
    获取树的深度
    :param root: 
    :return: 
    '''
    if not root:
        return 0
    max_depth = max(get_depth(root.lchild),get_depth(root.rchild))+1
    return max_depth

if __name__ == "__main__":
    # 遍历结果错误，原因？？？
    list_node = []
    list_node = create_tree()
    root = create_Haffman(list_node)
    print("lchild:%s node:%s rchild:%s")%(root.lchild.val,root.val,root.rchild.val)
    node_in_result = []
    recursion_in(root,node_in_result) #错误 正确[40, 100, 5, 15, 10, 30, 15, 60, 30]
    print("中序遍历结果：")
    print(node_in_result)

    node_pre_result = []
    recursion_pre(root,node_pre_result) #错误 正确[100, 40, 60, 30, 15, 5, 10, 15, 30]
    print("前序遍历结果：")
    print(node_pre_result)

    tree_dept = get_depth(root)
    print("树最大深度:")
    print(tree_dept)







