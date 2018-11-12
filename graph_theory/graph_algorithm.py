# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj

from graph_theory.graphAL import GraphAL
from deque.prio_queue import PrioQueue

inf = float("inf")


# Kruskal算法实现最小生成树，类似于层次聚类，选择最短路径每次合并两类
def Kruskal(graph):
    vnum = graph.vertex_num()
    # reps存入各顶点的初始集合
    reps = [i for i in range(vnum)]
    mst, edges = [], []
    # 把所有的边存入edges中
    for vi in range(vnum):
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    # 按权重、顶点排序
    edges.sort()
    for w, vi, vj in edges:
        # 如果vi和vj顶点所代表的集合不同
        if reps[vi] != reps[vj]:
            mst.append(((vi, vj), w))
            if len(mst) == vnum - 1:
                break
            # 把reps[?]==reps[vj]的全部换成reps[vi]
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):
                if reps[i] == orep:
                    reps[i] = rep
    return mst


# 最小生成树算法，从一个顶点出发扩大集合
def Prim(graph):
    vnum = graph.vertex_num()
    mst = [None] * vnum
    # 优先队列！！！！！！！
    cands = PrioQueue([(0, 0, 0)])
    count = 0
    while count < vnum and not cands.is_empty():
        w, u, v = cands.dequeue()
        if mst[v]:
            continue
        mst[v] = ((u, v), w)
        count += 1
        for vi, w in graph.out_edges(v):
            if not mst[vi]:
                cands.enqueue((w, v, vi))
    return mst


# 最短路径算法，v0至任意点的最短路径，巧在使用了优先队列
def dijkstra_shortest_paths(graph, v0):
    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    paths = [None] * vnum
    count = 0
    cands = PrioQueue([(0, v0, v0)])
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()
        if paths[vmin]:
            continue
        # 最短路径的上一个顶点及长度
        paths[vmin] = (u, plen)
        for v, w in graph.out_edges(vmin):
            if not paths[v]:
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return paths


# Floyd算法，得到任意两点间的最短距离
def all_shortest_path(graph):
    vnum = graph.vertex_num()
    a = [[graph.get_edge(i, j) for j in range(vnum)] for i in range(vnum)]
    nvertex = [[-1 if a[i][j] == inf else j for j in range(vnum)] for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nvertex[i][j] = nvertex[i][k]
    return a, nvertex


# 拓扑排序
def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq = [0] * vnum, []
    zerov = -1
    for vi in range(vnum):
        for v, w in range(vnum):
            indegree[v] += 1
    for vi in range(vnum):
        if indegree[vi] == 0:
            indegree[vi] = zerov
            zerov = vi
    for n in range(vnum):
        if zerov == -1:
            return False
        vi = zerov
        zerov = indegree[zerov]
        toposeq.append(vi)
        for v, w in graph.out_edges(vi):
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] = zerov
                zerov = v
    return toposeq


if __name__ == "__main__":
    mat = [[0, 5, 11, 5, 0, 0, 0], [5, 0, 0, 3, 9, 0, 7],
           [11, 0, 0, 7, 0, 6, 0], [5, 3, 7, 0, 0, 0, 20],
           [0, 9, 0, 0, 0, 0, 8], [0, 0, 6, 0, 0, 0, 8],
           [0, 7, 0, 20, 8, 8, 0]]
    graph01 = GraphAL(mat)
    print("图graph01：")
    print(graph01)
    print("Kruskal算法最小生成树：")
    mst = Kruskal(graph01)
    print(mst)
    mst1 = Prim(graph01)
    print("Prim算法最小生成树：")
    print(mst1)
    dij = dijkstra_shortest_paths(graph01, 0)
    print("Dijkstra算法求最短路径：")
    print(dij)
    print("Floyd算法求最短路径：")
    arr, paths = all_shortest_path(graph01)
    print(arr, '\n', paths)
