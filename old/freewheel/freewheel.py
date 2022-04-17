"""
-*- coding: utf-8 -*-
@File  : freewheel.py
@Time  : 2022/4/16
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：

"""


class Solution:
    def antiSpiralOrder(self, matrix):
        # # [::-1]为倒序输出的意思，也就实现了水平翻转
        # matrix[:] = matrix[::-1]
        # # zip用于将矩阵打包为元组的列表，实现转置功能，加上*号可以将元组转为矩阵
        # test2 = zip(*matrix)
        # test3 = map(list, test2)
        # test4 = list(test3)
        # 顺时针旋转90度，通过先水平翻转再转置来实现
        matrix[:] = list(zip(*(matrix[::-1])))
        # 转置
        matrix = list(zip(*matrix))
        # 输出第一行
        res = list(matrix.pop(0))
        while matrix:
            # 逆时针旋转90度，通过先转置后水平翻转实现
            matrix = list(zip(*matrix))[::-1]
            res += list(matrix.pop(0))
        return res


s = Solution()
test = s.antiSpiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(test)


# class Solution:
#     def longestGeometricSeqLength(self, nums):
#         n = len(nums)
#         if n < 3:
#             return n
#         dp = [{} for i in range(n)]
#         result = 0
#         for i in range(n):
#             for j in range(i):
#                 div = nums[i] / nums[j]
#                 if div not in dp[j]:
#                     dp[i][div] = 2
#                 else:
#                     dp[i][div] = dp[j][div] + 1
#                 result = max(result, dp[i][div])
#         return result
#
#
# s = Solution()
# test = s.longestGeometricSeqLength([75, 72, 27, 25, 5, 9, 12, 1, 3, 1])
# print(test)















