# -*- coding: utf-8 -*-
"""
@File: 最长回文子串.py
@Time: 2022/4/19 16:41
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：对于一个子串而言，如果它是回文串，并且长度大于 2，那么将它首尾的两个字母去除之后，它仍然是个回文串。例如对于字符串“ababa”，
如果我们已经知道 “bab” 是回文串，那么 “ababa” 一定是回文串，这是因为它的首尾两个字母都是“a”。
关键点：构建dp二维矩阵，状态转移方程 dp[i][j] = (s[i]==s[j]) and (j-i<3 or dp[i+1][j-1]) 注意j-i<3这一边界条件
输入：
babad
输出：
"bab"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 1
        begen = 0
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        for j in range(1, n):
            for i in range(0, j):
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if (j - i) < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                if dp[i][j] and j-i+1 > max_len:
                    begen = i
                    max_len = j-i+1
        result = s[begen:begen+max_len]
        return result


ss = input()
s = Solution()
result = s.longestPalindrome(ss)
print(result)








