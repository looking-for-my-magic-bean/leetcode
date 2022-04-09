"""
-*- coding: utf-8 -*-
@File  : single-number.py
@Time  : 2022/3/29
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

关键点在于0异或其他数为其他数，两个相同的数异或则为0。

"""


class Solution:
    def singleNumber(self, nums) -> int:

        out = 0
        for num in nums:
            out = out ^ num
        return out


s = Solution()
test = s.singleNumber([2,2,3,4,5,4,3])
print(test)
