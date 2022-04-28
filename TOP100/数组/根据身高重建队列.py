# -*- coding: utf-8 -*-
"""
@File: 根据身高重建队列.py
@Time: 2022/4/28 16:37
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：先第一队列与第二队列反向排序，根据第二位指示的是大于等于当前第一位元素的个数，由于排序后的数小于等于前面的数，所以往前插入不会影响前面已经拍好的序列。
输入：
[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]
输出：
[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]):
        res = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            else:
                res.insert(p[1], p)
        return res


nums = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
solution = Solution()
res = solution.reconstructQueue(nums)
print(res)
