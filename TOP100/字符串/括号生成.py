"""
-*- coding: utf-8 -*-
@File  : 括号生成.py
@Time  : 2022/4/21
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：添加(后进入递归之后再pop操作，
暴力和回溯的不同就在于验证列表是否符合规范是用额外函数验证还是在添加元素本身上做限制
输入：
3
输出：
["((()))","(()())","(())()","()(())","()()()"]
"""


# class Solution:
#     def generateParenthesis(self, n: int):
#         def generate(A):
#             if len(A) == 2*n:
#                 if valid(A):
#                     # 如果A的验证没有问题，则将A连起来形成一个完整的组合
#                     ans.append("".join(A))
#             else:
#                 A.append('(')
#                 generate(A)
#                 A.pop()
#                 A.append(')')
#                 generate(A)
#                 A.pop()
#
#         def valid(A):
#             bal = 0
#             for c in A:
#                 if c == '(':
#                     bal += 1
#                 else:
#                     bal -= 1
#                 # 多余的 ) 在 ( 之前出现了，后面就不需要看了
#                 if bal < 0:
#                     return False
#             return bal == 0
#
#         ans = []
#         generate([])
#         return ans


class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                # 将S的有效性检验放到函数内部去实现，能到2*n个字符时一定是有效的
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans


num = int(input())
s = Solution()
result = s.generateParenthesis(num)
print(result)
