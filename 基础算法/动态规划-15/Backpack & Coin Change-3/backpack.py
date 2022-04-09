# -*- coding: utf-8 -*-
"""
@File: backpack.py
@Time: 2022/4/4 21:22
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：
10
3,4,8,5
输出：
9

这个题可以和背包问题2合并为同一个问题，val列表在此题中与所占体积相同，在2中代表元素所含价值。
核心为两步：
1、当前背包容量是否能装下当前枚举元素？
    若不能则当前n个元素的最大大价值与前n-1个元素的相同
2、若能够装下，问题进一步为要不要装下？（比较装和不装的后果，看谁价值最大）
    若要装下则当前n个元素的最大价值等于当前背包容量减去当前元素体积后的背包容量和前n-1个元素对应的最大价值加当前元素价值。
    若不装下则当前n个元素的最大大价值与前n-1个元素的相同

"""

m = int(input())
a = list(map(int, input().split(",")))


class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param a: Given n items with size A[i]
    @return: The maximum size
    """
    def back_pack(self, m: int, a) -> int:
        # write your code here
        val = a.copy()
        n = len(a)
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if j < a[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-a[i-1]] + val[i-1])
        return dp[n][m]


s = Solution()
test = s.back_pack(m, a)
print(test)
