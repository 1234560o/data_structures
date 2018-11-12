# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:zwj

from graph_theory.graph_class import GraphError, Graph
from graph_theory.graph_traverse import DFS_graph, DFS_span_forest


class GraphAL(Graph):
    def __init__(self, mat=[], unconn=0):
        # super().__init__(self, )
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:
                raise ValueError("Argument for GraphAL.")
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError("Cannot add edge to empty graph.")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not valid vertex")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)
                return
            if row[i][0] > vj:
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not valid vertex")
        if vi == vj:
            return self._unconn
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return float('inf')

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex.")
        return self._mat[vi]


if __name__ == "__main__":
    mat = [[0, 2, 0, 3, 4], [2, 0, 2, 0, 0], [0, 2, 0, 0, 0],
           [3, 0, 0, 0, 1], [4, 0, 0, 1, 0]]
    graph = Graph(mat)
    print(graph)
    graph01 = GraphAL(mat)
    print(graph01)
    print("输出顶点0的邻接点：")
    print(graph01.out_edges(0))
    print("增加一个顶点：")
    print(graph01.add_vertex())
    graph01.add_edge(2, 5, 10)
    graph01.add_edge(5, 2, 10)
    print(graph01)
    print("深度遍历：")
    print(DFS_graph(graph01, 0))
    print("递归构造DFS生成树：")
    print(DFS_span_forest(graph01))
