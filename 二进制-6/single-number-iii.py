"""
-*- coding: utf-8 -*-
@File  : single-number-iii.py
@Time  : 2022/3/29
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

核心思想是利用两个单数异或出来的数来将原数组分为两组，每组中带有一个单数。（两个数异或为1的位做筛选）

"""


class Solution:
    def singleNumber(self, nums):
        tmp = 0
        for num in nums:
            tmp ^= num  # 最终异或出来的是两个单数的异或值
        i = 0
        while tmp & 1 == 0:  # 确认异或的结果从右边数第一个出现的1在第几位
            tmp = tmp >> 1
            i += 1
        tmp = 1 << i  # 用于分组的二进制数

        first, second = 0, 0
        for num in nums:  # 用tmp将数组中的数分为两组，偶数出现次数的数会自己异或消除
            if tmp & num:
                first ^= num
            else:
                second ^= num
        return [first, second]


s = Solution()
test = s.singleNumber([2, 2, 3, 4, 4, 5])
print(test)
