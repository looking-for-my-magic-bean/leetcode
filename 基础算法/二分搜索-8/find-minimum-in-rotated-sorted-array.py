# -*- coding: utf-8 -*-
"""
@Time: 2022/3/7 22:52
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

此题的关键点在于发现规律，找到判断点为nums[m]和nums[r]做对比。nums[m]>nums[r]，最小点在右边，反之左边。

"""


class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[0]
        while l < r:
            m = (l + r) >> 1
            if nums[m] > nums[r]:  # nums[m]不可能等于nums[r]，所以l必须为m+1。
                l = m + 1
            else:
                r = m
        return nums[l]


test_list = [3,4,5,1,2]
test = Solution()
result = test.findMin(test_list)
print(result)
