"""
-*- coding: utf-8 -*-
@File  : single-number-ii.py
@Time  : 2022/3/29
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""


# class Solution:
#     def singleNumber(self, nums) -> int:
#         seen_once = seen_twice = 0
#
#         for num in nums:
#             seen_once = ~seen_twice & (seen_once ^ num)
#             seen_twice = ~seen_once & (seen_twice ^ num)
#
#         return seen_once


class Solution:
    def singleNumber(self, nums) -> int:
        nums_set = set(nums)
        ans = 0
        for i in nums_set:
            ans += i
        ans = ans * 3
        all = sum(nums)
        count = (ans - all) // 2
        return count


s = Solution()
test = s.singleNumber([2,2,3,2,4,4,4])
print(test)
