"""
-*- coding: utf-8 -*-
@File  : balanced-binary-tree.py
@Time  : 2022/4/7
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
3,9,20,null,null,15,7
输出：
true

"""

from main import list_to_binarytree

nums = input().split(",")

binary_tree = list_to_binarytree(nums)


class Solution:
    def isBalanced(self, root) -> bool:
        def find(root):
            if root is None:
                return 0, True
            l_high, l = find(root.left)
            r_high, r = find(root.right)
            return 1+max(l_high, r_high), abs(l_high - r_high) < 2 and l and r
        return find(root)[1]


s = Solution()
result = s.isBalanced(binary_tree)
print(result)
