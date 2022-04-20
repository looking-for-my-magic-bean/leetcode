# -*- coding: utf-8 -*-
"""
@File: 无重复字符的最长子串.py
@Time: 2022/4/20 10:48
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：


"""


# # 暴力解法，对每个字符串作为开头去遍历后面的字符串
# class Solution:
#     def lengthOfLongestSubstring(self, s: str):
#         n = len(s)
#         if n == 0:
#             return 0
#         max_length = 1
#         temp = {}
#         for i in range(n-1):
#             temp.clear()
#             temp[s[i]] = True
#             temp_length = 1
#             for j in range(i+1, n):
#                 if s[j] in temp:
#                     break
#                 else:
#                     temp[s[j]] = True
#                     temp_length += 1
#                     max_length = max(temp_length, max_length)
#         return max_length
# 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str):
        n = len(s)
        rk, max_length = -1, 0
        temp = set()
        if n == 0:
            return 0
        for i in range(n):
            if i != 0:
                temp.remove(s[i-1])
            while rk+1 < n and s[rk+1] not in temp:
                temp.add(s[rk+1])
                rk += 1
            max_length = max(max_length, rk-i+1)
        return max_length


ss = input()
s = Solution()
result = s.lengthOfLongestSubstring(ss)
print(result)

