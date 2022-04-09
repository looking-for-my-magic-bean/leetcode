"""
-*- coding: utf-8 -*-
@File  : longest-consecutive-sequence.py
@Time  : 2022/4/5
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
100,4,200,1,3,2
输出：
4

"""

nums = list(map(int, input().split(",")))


class Solution:
    def longestConsecutive(self, nums) -> int:
        longest_streak = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_streak = 1

                while num + 1 in nums:
                    num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


s = Solution()
test = s.longestConsecutive(nums)
print(test)
