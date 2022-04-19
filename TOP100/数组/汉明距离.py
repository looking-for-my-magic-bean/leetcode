# -*- coding: utf-8 -*-
"""
@File: 汉明距离.py
@Time: 2022/4/19 15:03
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：求汉明距离能够想到异或操作，之后就是统计该数转换为二进制后的含有多少个1了
输入：
1
4
输出：
2

"""
import collections


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        z_bit = bin(z)
        result = collections.Counter(z_bit)
        return result["1"]


x = int(input())
y = int(input())
s = Solution()
result = s.hammingDistance(x, y)
print(result)

