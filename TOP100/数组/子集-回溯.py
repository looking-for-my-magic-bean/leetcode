# -*- coding: utf-8 -*-
"""
@File: 子集-回溯.py
@Time: 2022/4/28 10:19
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：
运用回溯法解决，关键问题在递归方程中深度的设置，由于此题没有重复元素且只需要向后寻找，在递归时深度也代表了可寻找范围
输入：
1, 2, 3
输出：
[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]

"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, depth, path):
            res.append(path.copy())

            for i in range(depth, n):
                path.append(nums[i])
                dfs(nums, i + 1, path)  # 只需要往当前i所在位置的后面寻找元素
                path.pop()

        n = len(nums)
        if len(nums) == 0:
            return []
        res = []
        dfs(nums, 0, [])
        return res


nums = [1, 2, 3]
solution = Solution()
res = solution.subsets(nums)
print(res)
