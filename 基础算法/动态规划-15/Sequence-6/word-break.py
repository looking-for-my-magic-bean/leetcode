# -*- coding: utf-8 -*-
"""
@File: word-break.py
@Time: 2022/4/3 11:35
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm



"""


class Solution:
    def wordBreak(self, s, wordDict) -> bool:
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in range(i+1, n+1):
                    if(s[i:j] in wordDict):
                        dp[j] = True

        return dp[-1]


s = Solution()
test = s.wordBreak("leetcode", ["leet", "code"])
print(test)
