# -*- coding: utf-8 -*-
"""
@Time: 2022/3/7 22:52
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

此题的关键点是多了相同的数来增加复杂度，只要对相同的数增加一个处理流程，让右边界直接减一实现循环。
另外，只是中间和右边相等，不能确定左边也相等，所以不能直接返回左边界，所以返回左边界和右边界都是不对的，减一循环才是正确的。
"""


class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) >> 1
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1  # 此处的操作是对源r进行减一操作，而r=r-1是新产生了另一个r来进行赋值
        return nums[l]


test_list = [0,1,1,0]
test = Solution()
result = test.findMin(test_list)
print(result)
