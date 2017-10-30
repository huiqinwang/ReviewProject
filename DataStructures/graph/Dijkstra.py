#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-16 下午9:29
# @Author  : huiqin
# @File    : Dijkstra.py
# @Description : Class is for
# 邻接矩阵表示图
# 初始顶点集合
from numpy import *
import math
INFINITY = 65535                        #代表无穷大
vexs = array([[0,10,INFINITY,INFINITY,INFINITY,11,INFINITY,INFINITY,INFINITY],#邻接矩阵
        [10,0,18,INFINITY,INFINITY,INFINITY,16,INFINITY,12],
        [INFINITY,18,0,22,INFINITY,INFINITY,INFINITY,INFINITY,8],
        [INFINITY,INFINITY,22,0,20,INFINITY,INFINITY,16,21],
        [INFINITY,INFINITY,INFINITY,20,0,26,INFINITY,7,INFINITY],
        [11,INFINITY,INFINITY,INFINITY,26,0,17,INFINITY,INFINITY],
        [INFINITY,16,INFINITY,24,INFINITY,17,0,19,INFINITY],
        [INFINITY,INFINITY,INFINITY,16,7,INFINITY,19,0,INFINITY],
        [INFINITY,12,8,21,INFINITY,INFINITY,INFINITY,INFINITY,0]])

lengthVex = len(vexs)                   #邻接矩阵大小
adjvex = zeros(lengthVex)               #连通分量，初始只有第一个顶点，当全部元素为1后，说明连通分量已经包含所有顶点
adjvex[0] = 1;
lowCost = vexs[0,:]                     #记录与连通分量连接的顶点的最小权值，初始化为与第一个顶点连接的顶点权值
lowCost[0] = 0
lastLowCost = ones(lengthVex)*INFINITY
lastLowCost[0] = 0
count = 0
path = [INFINITY]*lengthVex
I = 0
while (count<lengthVex):
    lastI = I
    I = (argsort(lowCost))[count]
    print("Vertex   [",count,"]:",I)
    adjvex[I] = lowCost[I]
    print("Edge [",count,"]:",adjvex[I])
    lowCost = array(list(map(lambda x,y:x if x<y else y,lowCost,vexs[I,:])))
    flag = list(map(lambda x,y: x==y, lowCost,lastLowCost))
    flag[I] = True
    print(flag)
    path = list(map(lambda x,y,z:y if x else z,flag,path,list([I])*lengthVex))
    print(path)
    lastLowCost = lowCost
    count = count+1
minPath = []
temp = 4
while path[temp]<INFINITY:
    minPath.append([temp,path[temp]])
    temp = path[temp]
print("minPath",minPath)


