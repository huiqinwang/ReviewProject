#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-17 上午11:04
# @Author  : huiqin
# @File    : HaffmanCoding.py
# @Description : Class is for
class Node:
    def __init__(self,freq=-1):
        self.freq = freq
        self.lchild = None
        self.rchild = None
        self.father = None

    def islchild(self):
        return self.father.lchild == self

def create_nodes(freq_list):
    '''
    构建带有权值的结点
    :param freq_list: 
    :return: 
    '''
    return [Node(freq) for freq in freq_list]

def sort_nodes(node_list):
    '''
    按照权值对结点排序，升序
    :param node_list: 
    :return: 
    '''
    return sorted(node_list,key=lambda node:node.freq)

def create_Haffman(node_lists):
    '''
    构造Haffman树
    :param node_list: 
    :return: 
    '''
    node_list = node_lists[:]
    while len(node_list) > 1:
        node_list = sort_nodes(node_list)
        lchild = node_list.pop(0)
        rchild = node_list.pop(0)
        new = Node()
        new.freq = lchild.freq+rchild.freq
        new.lchild = lchild
        new.rchild = rchild
        lchild.father = new
        rchild.father = new
        print("lchild.val:%s root.val:%s rchild.val:%s") % (new.lchild.freq, new.freq, new.rchild.freq)
        node_list.append(new)
    root = node_list.pop(0)
    return root

def haffman_coding(root,nodes):
    '''
    Haffman编码，思路：对每个叶结点一直查找到root，过程判断左右加入0或1
    :param root: 
    :param nodes: 
    :return: 
    '''
    codes = ['']*len(nodes)
    for i in range(len(nodes)):
        node = nodes[i]
        # print("lchild.val:%s root.val:%s rchild.val:%s") % (node.lchild.freq, node.freq, node.rchild.freq)
        while node != root:
            if node.islchild():   #为啥当node.islchild返回的是类此函数，不为None。这边要用node.islchild()
                codes[i] = '0'+codes[i]
            else:
                codes[i] = '1'+codes[i]
            node = node.father
    return codes

if __name__ == "__main__":
    freq_chars = [('C', 2), ('G', 2), ('E', 3), ('K', 3), ('B', 4),
                   ('F', 4), ('I', 4), ('J', 4), ('D', 5), ('H', 6),
                   ('N', 6), ('L', 7), ('M', 9), ('A', 10)]
    nodes = [item[1] for item in freq_chars]
    node_lists = create_nodes(nodes)
    print(len(node_lists))
    root = create_Haffman(node_lists)
    print("lchild.val:%s root.val:%-2s rchild.val:%s")%(root.lchild.freq,root.freq,root.rchild.freq)
    codes = haffman_coding(root,node_lists) #错误
    print(len(codes))
    for item in zip(freq_chars,codes):
        print(item)




