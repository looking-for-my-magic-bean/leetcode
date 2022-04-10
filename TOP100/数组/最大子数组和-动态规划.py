"""
-*- coding: utf-8 -*-
@File  : 最大子数组和-动态规划.py
@Time  : 2022/4/10
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
-2,1,-3,4,-1,2,1,-5,4
输出：
6
"""
nums = list(map(int, input().split(",")))


class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        temp = nums[-1]
        max_num = temp
        for i in range(n-2, -1, -1):
            temp = temp + nums[i] if temp > 0 else nums[i]
            max_num = max(max_num, temp)

        return max_num


s = Solution()
result = s.maxSubArray(nums)
print(result)
