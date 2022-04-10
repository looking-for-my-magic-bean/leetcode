"""
-*- coding: utf-8 -*-
@File  : 反转二叉树-递归.py
@Time  : 2022/4/10
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
[4,2,7,1,3,6,9]
输出：
[4,7,2,9,6,3,1]
核心思想：递归，将左右节点互换

"""
from main import list_to_binarytree


class Solution:
    def invertTree(self, root):
        if root is None:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


root = list_to_binarytree([4,2,7,1,3,6,9])
s = Solution()
result = s.invertTree(root)
print(result)
