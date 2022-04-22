"""
-*- coding: utf-8 -*-
@File  : 盛最多水的容器-双指针.py
@Time  : 2022/4/22
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：采用双指针的思想，左右指针分别指示数组的两个边界，每一次改变都向不可能更糟糕的情况去改变。
输入：
1,8,6,2,5,4,8,3,7
输出：
49
"""


# class Solution:
#     def maxArea(self, height):
#         result = 0
#         max_result = 0
#         n = len(height)
#         for i in range(n):
#             max_height = height[i]
#             for j in range(n-1, i, -1):
#                 if height[j] >= max_height:
#                     result = (j-i)*max_height
#                     max_result = max(result, max_result)
#                     break
#                 else:
#                     result = (j-i)*height[j]
#                     max_result = max(result, max_result)
#         return max_result

class Solution:
    def maxArea(self, height):
        area = 0
        max_area = 0
        l, r = 0, len(height)-1
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            max_area = max(area, max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


nums = list(map(int, input().split(",")))
s = Solution()
result = s.maxArea(nums)
print(result)
