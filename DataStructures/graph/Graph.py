#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-17 下午2:57
# @Author  : huiqin
# @File    : Graph.py
# @Description : Class is for

# 无向图　利用字典存储图
class Graph:
    def __init__(self):
        self.node_neighbors = {}

    def add_nodes(self,node_list):
        for node in node_list:
            self.add_node(node)

    def add_node(self,node):
        if node not in self.node_neighbors.keys():
            self.node_neighbors[node] = []

    def add_edge(self,egde):
        v,u = egde
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if v!=u:
                self.node_neighbors[v].append(u)

    def get_nodes(self):
        return self.node_neighbors.keys()