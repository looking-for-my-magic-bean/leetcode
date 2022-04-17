"""
-*- coding: utf-8 -*-
@File  : 旋转图像.py
@Time  : 2022/4/17
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：
顺时针旋转：先水平翻转，再转置
逆时针旋转：先转置，再水平翻转
输入：

输出：

"""


class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = list(zip(*(matrix[::-1])))

