"""
-*- coding: utf-8 -*-
@File  : jump-game.py
@Time  : 2022/3/31
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

核心思想：从后向前确定前一个是否能到达

"""


class Solution:
    def canJump(self, nums) -> bool:
        m = len(nums)
        left = m - 1

        for i in range(m-2, -1, -1):
            left = i if i + nums[i] >= left else left

        return left == 0


s = Solution()
test = s.canJump([2,3,1,1,4])
print(test)
