"""
-*- coding: utf-8 -*-
@File  : 移动零-双指针.py
@Time  : 2022/4/10
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
0,1,0,3,12
输出：
[1,3,12,0,0]
"""
nums = list(map(int, input().split(",")))


class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, 0
        n = len(nums)
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
        return nums


s = Solution()
result = s.moveZeroes(nums)
print(result)
