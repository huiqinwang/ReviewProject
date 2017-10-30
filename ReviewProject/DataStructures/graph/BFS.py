#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-16 下午9:15
# @Author  : huiqin
# @File    : BFS.py
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

def BFS(node,graph,results):
    '''
    深度优先遍历图
    :param nodes: 
    :param graph: 
    :return: 
    '''
    visits = {}
    visits[id(node)] = 1
    queues = []
    queues.append(node)
    while queues:
        node_tmp = queues.pop(0)
        results.append(node_tmp)
        for item in graph.node_neighbors[node_tmp]:
            if id(item) not in visits:
                visits[id(item)] = 1
                queues.append(item)
    return results



if __name__ == "__main__":
    graph = Graph()
    graph = create_graph()
    nodes = graph.get_nodes()
    node = nodes[0]
    results = []
    results = BFS(nodes[0],graph,results)
    # 正确：[1, 2, 3, 4, 5, 6, 7, 8]
    print(results)