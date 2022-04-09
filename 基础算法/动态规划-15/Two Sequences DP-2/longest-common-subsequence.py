# -*- coding: utf-8 -*-
"""
@File: longest-common-subsequence.py
@Time: 2022/4/4 10:34
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：
"abcde"
"ace"
输出：
3


"""
s1 = eval(input())  # eval() 函数用于去掉输入的引号
s2 = eval(input())


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]


s = Solution()
test = s.longestCommonSubsequence(s1, s2)
print(test)
