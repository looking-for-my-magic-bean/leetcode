# -*- coding: utf-8 -*-
"""
@File: coin-change.py
@Time: 2022/4/4 11:08
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：
[1,2,5]
11
输出：
3

strip() 方法用于移除字符串头尾指定的字符（默认为空格）。

"""
coins = list(map(int, input().split(',')))  # 先input读取输入字符串（,分隔读取），之后将读取到的数映射为int，然后转为list。
amount = int(input())


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


s = Solution()
test = s.coinChange(coins, amount)
print(test)
