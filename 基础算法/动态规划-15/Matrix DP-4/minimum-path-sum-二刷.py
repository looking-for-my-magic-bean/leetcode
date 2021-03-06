"""
-*- coding: utf-8 -*-
@File  : minimum-path-sum-二刷.py
@Time  : 2022/3/30
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

核心思想：自下向上，寻找能到当前元素的可选路径和的最小值加上当前元素值作为到达当前元素的最小路径和。

"""


class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if i+1 > m-1:
                    grid[i][j] += grid[i][j+1]
                elif j+1 > n-1:
                    grid[i][j] += grid[i+1][j]
                else:
                    grid[i][j] += min(grid[i][j+1], grid[i+1][j])
        return grid[0][0]


s = Solution()
test = s.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(test)
