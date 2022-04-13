"""
-*- coding: utf-8 -*-
@File  : triangle-二刷.py
@Time  : 2022/3/30
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

核心思想: 自下向上遍历，当前元素节点值与其邻近的下层两个元素的值的最小和作为当前元素节点的值。


"""


class Solution:
    def minimumTotal(self, triangle):

        n = len(triangle)
        if n == 0:
            return 0

        dp = triangle[-1].copy()

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


s = Solution()
test = s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
print(test)
