"""
-*- coding: utf-8 -*-
@File  : 买卖股票的最佳时机-动态规划.py
@Time  : 2022/4/10
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
7,1,5,3,6,4
输出：
5

"""
nums = list(map(int, input().split(",")))


class Solution:
    def maxProfit(self, prices) -> int:
        minPrice = float("inf")
        maxProfit = 0
        for price in prices:
            Profit = price - minPrice
            minPrice = min(price, minPrice)
            maxProfit = max(Profit, maxProfit)
        return maxProfit


s = Solution()
result = s.maxProfit(nums)
print(result)
