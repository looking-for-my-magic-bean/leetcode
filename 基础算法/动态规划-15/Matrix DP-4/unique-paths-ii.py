"""
-*- coding: utf-8 -*-
@File  : unique-paths-ii.py
@Time  : 2022/3/31
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

核心思想：自下向上的进行遍历，路途中不断累积路径的数量，碰到有障碍的地方让其累积为 0

"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m , n = len(obstacleGrid), len(obstacleGrid[0])
        grid = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    if i == m-1 and j == n-1:
                        grid[i][j] = 1
                        continue
                    grid[i][j] = grid[i+1][j] + grid[i][j+1]

        return grid[0][0]


s = Solution()
test = s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
print(test)
