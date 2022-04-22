"""
-*- coding: utf-8 -*-
@File  : 合并区间.py
@Time  : 2022/4/22
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：后面出现的区间的开始值若小于之前的区间的结束值则可以进行合并，
合并后的区间的结束值是前后两个区间的结束值中较大的那个。
输入：
1 3
2 6
8 10
15 18
输出：
[[1,6],[8,10],[15,18]]
"""


class Solution:
    def merge(self, intervals):
        intervals.sort()
        result = []
        result.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])
        return result


nums = [[1,3],[2,6],[8,10],[15,18]]
s = Solution()
result = s.merge(nums)
print(result)
