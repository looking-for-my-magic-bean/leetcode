"""
-*- coding: utf-8 -*-
@File  : climbing-stairs.py
@Time  : 2022/3/31
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

核心思想：从下向上遍历，一共有两种步长，到达当前元素的所有可能路径等于向下两部和向下一步的所有可能的路径和

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        n = n + 1
        s = [0] * (n + 1)
        s[-2] = 1
        for i in range(n - 2, -1, -1):
            s[i] = s[i + 1] + s[i + 2]

        return s[0]


s = Solution()
test = s.climbStairs(2)
print(test)
