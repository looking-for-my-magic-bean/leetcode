# -*- coding: utf-8 -*-
"""
@File: redundant-connection.py
@Time: 2022/4/5 15:28
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：
[[1,2],[1,3],[2,3]]
输出：
[2,3]

"""


class Solution:
    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = list(range(n + 1))

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            parent[find(node1)] = find(node2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]

        return []


s = Solution()
test = s.findRedundantConnection([[1, ], [1, 3], [2, 3]])
print(test)
