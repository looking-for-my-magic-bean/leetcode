# -*- coding: utf-8 -*-
"""
@File: word-break.py
@Time: 2022/4/3 11:35
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

核心思想：建立辅助列表dp，记录每个循环开始的节点（元素内部为True的为开始节点），向后寻找字符串，看能不能找到最后。
关键点难点：由于dp长度比s长一个单位，要注意循环是i，j的取值。

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
