"""
-*- coding: utf-8 -*-
@File  : 螺旋矩阵.py
@Time  : 2022/4/17
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：
顺时针遍历：先输出第一行，再逆时针旋转90度，重复上述
逆时针遍历：先转置，输出第一行，再逆时针旋转90度，重复2,3步
输入：

输出：

"""


class Solution:
    def spiralOrder(self, matrix):
        result = matrix.pop(0)
        while matrix:
            matrix = list(zip(*matrix))[::-1]
            result += matrix.pop(0)
        return result
