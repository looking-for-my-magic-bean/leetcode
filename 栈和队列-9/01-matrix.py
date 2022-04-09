"""
-*- coding: utf-8 -*-
@File  : 01-matrix.py
@Time  : 2022/3/25
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""
from collections import deque


class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        new_mat = [[-1] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    new_mat[i][j] = 0
                    q.append((i, j))
        dist = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while q:
            i, j = q.popleft()
            for a, b in dist:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and new_mat[x][y] == -1:
                    new_mat[x][y] = new_mat[i][j] + 1
                    q.append((x, y))

        return new_mat


test = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
s = Solution()
print('new_matrix:', s.updateMatrix(test))
