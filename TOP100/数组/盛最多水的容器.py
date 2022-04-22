"""
-*- coding: utf-8 -*-
@File  : 盛最多水的容器.py
@Time  : 2022/4/22
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
1,8,6,2,5,4,8,3,7
输出：
49
"""


class Solution:
    def maxArea(self, height):
        result = 0
        max_result = 0
        n = len(height)
        for i in range(n):
            max_height = height[i]
            for j in range(n-1, i, -1):
                if height[j] >= max_height:
                    result = (j-i)*max_height
                    max_result = max(result, max_result)
                    break
                else:
                    result = (j-i)*height[j]
                    max_result = max(result, max_result)
        return max_result


nums = list(map(int, input().split(",")))
s = Solution()
result = s.maxArea(nums)
print(result)
