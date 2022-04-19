# -*- coding: utf-8 -*-
"""
@File: 最长等差or等比子序列.py
@Time: 2022/4/19 14:33
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：
# 75, 72, 27, 25, 5, 9, 12, 1, 3, 1
1, 3, 4, 6, 7, 9, 16, 12, 15, 27
输出：
4

"""

nums = list(map(int, input().split(",")))


class Solution:
    def longestGeometricSeqLength(self, nums):
        n = len(nums)
        if n < 3:
            return n
        dp = [{} for i in range(n)]
        result = 0
        for i in range(n):
            for j in range(i):
                div = nums[i] / nums[j]
                if div not in dp[j]:
                    dp[i][div] = 2
                else:
                    dp[i][div] = dp[j][div] + 1
                result = max(result, dp[i][div])
        return result


s = Solution()
test = s.longestGeometricSeqLength(nums)
print(test)
