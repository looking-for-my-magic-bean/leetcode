"""
-*- coding: utf-8 -*-
@File  : jump-game.py
@Time  : 2022/3/31
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

核心思想：从后向前遍历，对当前值寻找向后能到达的范围内的最小值
关键点：辅助数组除最后一位全部置为正无穷

"""


class Solution:
    def canJump2(self, nums):
        m = len(nums)
        s = [float('inf')] * m
        s[-1] = 0
        for i in range(m-2, -1, -1):
            s[i] = min(s[i:i+nums[i]+1]) + 1
        return s[0]


s = Solution()
test = s.canJump2([2, 3, 1, 1, 4])
print(test)
