# -*- coding: utf-8 -*-
"""
@Time: 2022/3/7 21:42
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

标准的方法是将right赋值的时候改成len(nums)，增加右边界，这样相当于mid的值增加了1，使得边界被拓宽了，left就是最后的结果。

解决方法二：这是另一种解法，如果现场想不起来通过增加右边界r来达到增加两边插入的效果的话可以用将两边插入的情况单独拎出来处理。

"""


class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left


class Solution2:
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        l, r = 0, len(nums)-1
        if target > nums[r]:
            return r + 1
        elif target < nums[l]:
            return 0
        else:
            while l < r:
                mid = (l + r) >> 1
                if target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            return l


test_list = [1,3,5,7]
val = 3
test = Solution()
result = test.searchInsert(test_list, val)
print(result)
