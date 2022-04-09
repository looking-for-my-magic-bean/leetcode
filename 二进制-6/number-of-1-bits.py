"""
-*- coding: utf-8 -*-
@File  : number-of-1-bits.py
@Time  : 2022/3/29
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        while n > 0:
            num_ones += 1
            n &= n - 1
        return num_ones


s = Solution()
test = s.hammingWeight(11)
print(test)
