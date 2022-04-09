# -*- coding: utf-8 -*-
"""
@Time: 2022/3/7 22:32
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

此题关键点在于二维数组如何映射为一维数组，(一维数组位置//列数，一位数组位置%列数)即可表示在二维数组中的对应位置。
divmod(位置，列数)函数返回前数除以后数的和前数对后数的取余，完美对应。

"""


class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left < right:
            mid = (left + right) >> 1
            x, y = divmod(mid, n)
            if matrix[x][y] >= target:
                right = mid
            else:
                left = mid + 1
        return matrix[left // n][left % n] == target

