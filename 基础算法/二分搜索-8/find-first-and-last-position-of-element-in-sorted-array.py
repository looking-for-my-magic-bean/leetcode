# -*- coding: utf-8 -*-
"""
@Time: 2022/3/7 13:23
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

二分寻找的基本架构是：
1、判断是否为空
2、赋值左右端点
3、while l < r 循环
4、mid = (left + right) >> 1 （右边界需要内部+1，mid = (left + right + 1) >> 1）
5、if判断语句，
   寻找左边界为目标值小于等于中点值， right = mid （等于的时候中点也要复制给右边）
   寻找右边界为目标值大于等于中点值， left = mid （等于的时候中点也要复制给左边）
6、left的值永远是要找的值的位置

"""


class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:         # 这一行函数是整个程序的关键点，等号的运用则是重中之重，目标值小于等于中点值决定了是向左找左边界(在等于时中点作为右边界，继续向左寻找可能值)
                right = mid
            else:
                left = mid + 1
        if nums[left] != target:
            return [-1, -1]
        l, right = left, len(nums) - 1
        while left < right:
            mid = (left + right + 1) >> 1  # 注意这里的mid求值要内部加1
            if nums[mid] <= target:        # 这一行函数是整个程序的关键点，等号的运用则是重中之重，目标值大于等于中点值决定了是向右找右边界(在等于时中点作为左边界，继续向右寻找可能值)
                left = mid
            else:
                right = mid - 1
        return [l, left]


test_list = [5,7,8,8,8,8,10]
val = 8
test = Solution()
result = test.searchRange(test_list, val)
print(result)
