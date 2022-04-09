"""
-*- coding: utf-8 -*-
@File  : 快速排序.py
@Time  : 2022/3/17
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

快排的本质还是分治法
1、将开头作为中间值
2、从右边开始循环，将比中间值小的放到左边
3、从左边开始循环，将比中间值大的放到右边
4、完成一轮循环，将中间值放回队列（放入左边指向的位置）
5、通过左右递归实现分治

"""


class Solution:
    def Quick_Sort_q(self, nums, start, end):
        if start >= end:
            return
        left = start
        right = end
        mid = nums[left]
        while left < right:
            while left < right and nums[right] >= mid:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= mid:
                left += 1
            nums[right] = nums[left]
        nums[left] = mid
        self.Quick_Sort_q(nums, 0, left - 1)
        self.Quick_Sort_q(nums, left + 1, end)

    def Quick_Sort(self, nums):
        nums_len = len(nums)
        self.Quick_Sort_q(nums, 0, nums_len - 1)
        return nums


test_list = [1, 1, 2, 0, 3, 7, 9, 1, 3]
test = Solution()
result = test.Quick_Sort(test_list)
print(result)
