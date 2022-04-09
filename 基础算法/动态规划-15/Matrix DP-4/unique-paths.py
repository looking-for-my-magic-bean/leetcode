"""
-*- coding: utf-8 -*-
@File  : unique-paths.py
@Time  : 2022/3/31
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

核心思想：自下向上的进行遍历，路途中不断累积路径的数量

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    grid[i][j] = 1
                    continue
                grid[i][j] = grid[i+1][j] + grid[i][j+1]

        return grid[0][0]


s = Solution()
test = s.uniquePaths(3, 7)
print(test)
