# -*- coding: utf-8 -*-
"""
@Time: 2022/3/7 21:42
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

注意对结果类型的分类，关键点就在于向左走还是向右走
对比前一种，此题的关键点在于理清重复值出现对寻找所产生的影响，重复值只要不在两边，对判断不会产生影响，
因此只需要将重复值在两边的情况进行特殊处理即可

"""


class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            if nums[l] == nums[r] and nums[l] != target:  # 关键点所在
                l += 1
                r -= 1
                continue
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


test_list = [4,5,6,7,0,1,4]
val = 0
test = Solution()
result = test.search(test_list, val)
print(result)
