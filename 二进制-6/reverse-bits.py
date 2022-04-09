"""
-*- coding: utf-8 -*-
@File  : reverse-bits.py
@Time  : 2022/3/29
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""


class Solution:
    def reverse_10(self, num) -> int:

        if num > 0:
            ans = 0
            while num > 0:
                ans = ans * 10 + num % 10
                num = num // 10
        else:
            num = -num
            ans = 0
            while num > 0:
                ans = ans * 10 + num % 10
                num = num // 10
            ans = -ans
        return ans

    def reverse_2(self, num, k) -> int:

        num = int(num, 2)  # 二进制转10进制
        ans = 0
        for _ in range(k):
            ans = ans * 2 + num % 2
            num = num // 2
        return bin(ans).replace("0b", "")  # 10进制转二进制 replace(old, new)

    def reverse_2_bit(self, num, k):  # 用位的操作可以解决java中负数的问题，python没有这个问题
        num = int(num, 2)  # 二进制转10进制
        ans = 0
        for _ in range(k):
            ans = (ans << 1) | (num & 1)
            num = num >> 1
        return bin(ans).replace("0b", "")


s = Solution()
test_10 = s.reverse_10(-321)
test_2 = s.reverse_2('10000010100101000001111010011100', 32)
test_2_bit = s.reverse_2_bit('10000010100101000001111010011100', 32)
print(test_10)
print(test_2)
print(test_2_bit)
