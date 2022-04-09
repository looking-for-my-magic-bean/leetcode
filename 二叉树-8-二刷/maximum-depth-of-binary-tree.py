"""
-*- coding: utf-8 -*-
@File  : maximum-depth-of-binary-tree.py
@Time  : 2022/4/7
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
3,9,20,None,None,15,7
输出：
3

"""
from main import list_to_binarytree

nums = input().split(",") 

binary_tree = list_to_binarytree(nums)


class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        return 1 + max(l, r)


s = Solution()
result = s.maxDepth(binary_tree)
print(result)




