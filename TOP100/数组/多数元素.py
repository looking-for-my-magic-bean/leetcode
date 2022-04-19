# -*- coding: utf-8 -*-
"""
@File: 多数元素.py
@Time: 2022/4/19 14:48
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：统计列表中字符或者数字出现的次数
输入：
3,2,3
输出：
3

"""
import collections


class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        max_num = collections.Counter(nums).most_common(1)
        return max_num[0][0] if max_num[0][1] > n/2 else 0


nums = list(map(int, input().split(",")))
s = Solution()
result = s.majorityElement(nums)
print(result)
