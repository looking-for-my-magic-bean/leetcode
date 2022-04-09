"""
-*- coding: utf-8 -*-
@File  : counting-bits.py
@Time  : 2022/3/29
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

关键点是注意到第i个数如果：
是奇数，其1的个数是其一半的数的1的个数的加一，
是偶数，其1的个数是其一半的数的个数。

"""


class Solution:
    def countBits(self, n: int):
        result = [0] * (n + 1)
        for i in range(n+1):
            result[i] = result[i >> 1] + (i & 1)  # i&1用于检测i是否为偶数，偶数为0，奇数为1
        return result


s = Solution()
test = s.countBits(5)
print(test)

