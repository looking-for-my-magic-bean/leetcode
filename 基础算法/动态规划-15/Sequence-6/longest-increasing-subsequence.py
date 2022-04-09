# -*- coding: utf-8 -*-
"""
@File: longest-increasing-subsequence.py
@Time: 2022/4/3 10:09
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：10,9,2,5,3,7,101,18
输出：4

"""
nums = input().split(",")


class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


s = Solution()
test = s.lengthOfLIS(nums)
print(test)
