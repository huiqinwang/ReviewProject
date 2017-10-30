#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-16 下午9:28
# @Author  : huiqin
# @File    : Prime.py
# @Description : Class is for

# 邻接矩阵表示图
# 初始顶点集合
debug = 0
MAX_NUM = 10000
v_num = 6

grapharr=[[0,6,1,5,MAX_NUM,MAX_NUM],
          [6,0,5,MAX_NUM,3,MAX_NUM],
          [1,5,0,5,5,4],
          [5,MAX_NUM,5,0,MAX_NUM,2],
          [MAX_NUM,3,6,MAX_NUM,0,6],
          [MAX_NUM,MAX_NUM,4,2,6,0]]

U = [] #已被选择的顶，初始是随机选择的点
V = [] #图中未被选择的点

def init():
    '''
    初始化顶点集合
    :return: 
    '''
    i = 1
    while i <= v_num:
        V.append(i)
        i = i+1
    print("init:V",V)

def prime_start(start):
    '''
    构造初始化顶点集合
    :param start: 
    :return: 
    '''
    U.append(start)
    del V[V.index(start)]
    print("start:U\nV",(U,V))


def sort_edge(edge_list):
    '''
    对list排序，返回排序前的index
    :param edge_list: 
    :return: 
    '''
    min_num = MAX_NUM
    min_index = -1
    for i in range(len(edge_list)):
        if edge_list[i] < min_num:
            min_num = edge_list[i]
            min_index = i

    return  min_index

def prime_min():
    '''
    prime算法实现，比较边选择顶点
    :return: 
    '''
    edge_list = []
    closed_list = []
    for i in range(len(U)):
        u = U[i]
        for j in range(len(V)):
            v = V[j]
            temp_edge = grapharr[i][j]

            closed_edge = {'u':u,'v':v}
            if (temp_edge < MAX_NUM) and (temp_edge >0):
                print("temp_edge", temp_edge)
                edge_list.append(temp_edge)
                closed_list.append(closed_edge)

    min_index = sort_edge(edge_list)
    min_edge = closed_list[min_index]
    U.append(min_edge['v'])   #将最小边的点加入U中
    del V[V.index(min_edge['v'])]
    return min_edge

def prime_all():
    '''
    对所有顶点进行prime操作
    :return: 
    '''
    closed_edge = []
    while len(U) != v_num:
        min_edge = prime_min()
        closed_edge.append(min_edge)
    return closed_edge


if __name__ == "__main__":
    init()
    prime_start(1)
    closed_edge = []
    closed_edge = prime_all()
    print('U====',U)
    print('V====',V)
    print("==============closed_edge============")
    print(closed_edge)



# 第二个实现方法，更简洁

# INFINITY = 65535                        #代表无穷大
# vexs = array([[0,10,INFINITY,INFINITY,INFINITY,11,INFINITY,INFINITY,INFINITY],#邻接矩阵
#         [10,0,18,INFINITY,INFINITY,INFINITY,16,INFINITY,12],
#         [INFINITY,INFINITY,0,22,INFINITY,INFINITY,INFINITY,INFINITY,8],
#         [INFINITY,INFINITY,22,0,20,INFINITY,INFINITY,16,21],
#         [INFINITY,INFINITY,INFINITY,20,0,26,INFINITY,7,INFINITY],
#         [11,INFINITY,INFINITY,INFINITY,26,0,17,INFINITY,INFINITY],
#         [INFINITY,16,INFINITY,INFINITY,INFINITY,17,0,19,INFINITY],
#         [INFINITY,INFINITY,INFINITY,16,7,INFINITY,19,0,INFINITY],
#         [INFINITY,12,8,21,INFINITY,INFINITY,INFINITY,INFINITY,0]])
#
# lengthVex = len(vexs)                   #邻接矩阵大小
# adjvex = zeros(lengthVex)               #连通分量，初始只有第一个顶点，当全部元素为1后，说明连通分量已经包含所有顶点
# adjvex[0] = 1;
# lowCost = vexs[0,:]                     #记录与连通分量连接的顶点的最小权值，初始化为与第一个顶点连接的顶点权值
# lowCost[0] = 0
# count = 0
# while (count<9):
#     I = (argsort(lowCost))[count]
#     print("Vertex   [",count,"]:",I)
#     adjvex[I] = lowCost[I]
#     print("Edge [",count,"]:",adjvex[I])
#     lowCost[I] = 0
#     lowCost = array(list(map(lambda x,y:x if x<y else y,lowCost,vexs[I,:])))
#     count = count+1
# print("The length of the minimum cost spanning tree is: ", sum(adjvex))
#
