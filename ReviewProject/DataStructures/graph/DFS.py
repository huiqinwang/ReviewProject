#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-16 下午9:15
# @Author  : huiqin
# @File    : DFS.py
# @Description : Class is for
from Graph import Graph

def create_graph():
    '''
    创建图
    :return: 
    '''
    graph = Graph()
    node_list = [i for i in range(1,9)]
    graph.add_nodes(node_list)
    graph.add_edge((1, 2))
    graph.add_edge((1, 3))
    graph.add_edge((2, 4))
    graph.add_edge((2, 5))
    graph.add_edge((4, 8))
    graph.add_edge((5, 8))
    graph.add_edge((3, 6))
    graph.add_edge((3, 7))
    graph.add_edge((6, 7))
    nodes = graph.get_nodes()
    print(nodes)
    return graph

def DFS(node,graph,results,vists):
    '''
    深度优先遍历图
    :param nodes: 
    :param graph: 
    :return: 
    '''
    for item in graph.node_neighbors[node]:
        if id(item)not in visits:
            visits[id(item)] = 1
            results.append(item)
            DFS(item,graph,results,visits)

if __name__ == "__main__":
    graph = Graph()
    graph = create_graph()
    nodes = graph.get_nodes()
    node = nodes[0]
    results = []
    visits = {}
    results.append(node)
    visits[id(node)] = 1
    DFS(nodes[0],graph,results,visits)
    # 正确：[1, 2, 4, 8, 5, 3, 6, 7]
    print(results)