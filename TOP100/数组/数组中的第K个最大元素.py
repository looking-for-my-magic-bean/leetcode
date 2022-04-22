# -*- coding: utf-8 -*-
"""
@File: 数组中的第K个最大元素.py
@Time: 2022/4/22 16:08
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：这个题考察的是排序算法，可以复习一下归并，快排，堆排这三种排序算法
输入：
3,2,1,5,6,4
2
输出：


"""


class Solution:
    def findKthLargest(self, nums, k: int):
        nums.sort(reverse=True)
        return nums[k-1]


nums = list(map(int, input().split(",")))
k = int(input())
s = Solution()
result = s.findKthLargest(nums, k)
print(result)
