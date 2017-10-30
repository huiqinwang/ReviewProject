#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-15 下午3:44
# @Author  : huiqin
# @File    : Tree.py
# @Description : Class is for
from Node import Node
class Tree:
    def create_tree(self,node):
        '''
        构建树
        :param node: 
        :return: 当结点的两个孩子都是None时，停止递归，因为孩子为None的话，孩子的孩子肯定不能创建
        '''
        s = raw_input("please input node:\n")
        if s == "#":
            node = None
        else:
            node.val = s
            node.lchild = Node()
            self.create_tree(node.lchild)
            node.rchild = Node()
            self.create_tree(node.rchild)

    def get_tree_root(self):
        '''
        返回树的root结点
        :return: 
        '''
        root = Node()
        self.create_tree(root)
        return root

if __name__ == "__main__":
    pass
