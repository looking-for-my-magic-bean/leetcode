# -*- coding: utf-8 -*-
"""
@Time: 2022/3/7 21:42
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

有时用到二分搜索的题目并不会直接给你一个有序数组，它隐含在题目中，需要你去发现或者构造。
一类常见的隐含的二分搜索的问题是求某个有界数据的最值，以最小值为例，当数据比最小值大时都符合条件，
比最小值小时都不符合条件，那么符合/不符合条件就构成了一种有序关系，再加上数据有界，我们就可以使用二分搜索来找数据的最小值。
注意，数据的界一般也不会在题目中明确提示你，需要你自己去发现。
关键点：构建有序数列

"""


class Solution:
    def minEatingSpeed(self, piles, h) -> int:
        left, right = 1, max(piles)
        # 吃的理论速率可以从1到piles中最大数，代表一次吃一根（最耗时）和一次吃最大堆中所有根（最节时）根本目的还是为了找到最小的吃速率(target)
        while left < right:
            mid = (left + right) >> 1
            s = sum((pile + mid - 1) // mid for pile in piles)
            # 计算吃的速率为mid时所需要的时间总和，耗时多了代表要加快吃的速率，耗时少还可以减小吃速率，最终找到符合条件最小吃速率。
            # 注意，这里吃速率和总耗时成反比，吃的速率越大，耗时越小。
            if s <= h:  # 耗时少了，说明吃的速率大了，可以调小吃的速率，往左找
                right = mid
            else:
                left = mid + 1
        return left


test_list = [3,6,7,11]
val = 8
test = Solution()
result = test.minEatingSpeed(test_list, val)
print(result)
