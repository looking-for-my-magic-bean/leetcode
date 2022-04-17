"""
-*- coding: utf-8 -*-
@File  : freewheel.py
@Time  : 2022/4/16
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：

"""


# class Solution:
#     def antiSpiralOrder(self, matrix):
#         matrix = list(map(list, zip(*(matrix[::-1]))))
#         matrix = list(map(list, zip(*matrix)))
#         res = list(matrix.pop(0))
#         while matrix:
#             matrix = list(zip(*matrix))[::-1]
#             res += list(matrix.pop(0))
#         return res
#
#
# s = Solution()
# test = s.antiSpiralOrder([[1,2,3],[4,5,6],[7,8,9]])
# print(test)


class Solution:
    def longestGeometricSeqLength(self, nums):
        n = len(nums)
        if n < 3:
            return n
        dp = [{} for i in range(n)]
        result = 0
        for i in range(n):
            for j in range(i):
                div = nums[i] / nums[j]
                if div not in dp[j]:
                    dp[i][div] = 2
                else:
                    dp[i][div] = dp[j][div] + 1
                result = max(result, dp[i][div])
        return result


s = Solution()
test = s.longestGeometricSeqLength([75, 72, 27, 25, 5, 9, 12, 1, 3, 1])
print(test)















