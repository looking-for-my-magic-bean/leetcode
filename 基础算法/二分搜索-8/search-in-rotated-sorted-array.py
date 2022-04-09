# -*- coding: utf-8 -*-
"""
@Time: 2022/3/7 21:42
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

注意对结果类型的分类，关键点就在于向左走还是向右走

"""


class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if target < nums[l] and nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target > nums[r] and nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


test_list = [4,5,6,7,0,1,2]
val = 0
test = Solution()
result = test.search(test_list, val)
print(result)
