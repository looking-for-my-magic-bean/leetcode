"""
-*- coding: utf-8 -*-
@File  : clone-graph.py
@Time  : 2022/3/22
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

这个图的问题先略过

"""
from collections import deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, start: 'Node') -> 'Node':

        if start is None:
            return None

        visited = {start: Node(start.val, [])}
        bfs = deque([start])

        while len(bfs) > 0:
            curr = bfs.popleft()
            curr_copy = visited[curr]
            for n in curr.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val, [])
                    bfs.append(n)
                curr_copy.neighbors.append(visited[n])

        return visited[start]


adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
test = Solution()
result = test.cloneGraph(adjList)

