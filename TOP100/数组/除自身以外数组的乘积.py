# -*- coding: utf-8 -*-
"""
@File: 除自身以外数组的乘积.py
@Time: 2022/4/28 17:07
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：


"""
from typing import List


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        L = [1 for _ in range(n)]
        R = [1 for _ in range(n)]
        res = []
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
        for i in range(n):
            res.append(L[i] * R[i])
        return res


nums = [1,2,3,4]
solution = Solution()
res = solution.productExceptSelf(nums)
print(res)
