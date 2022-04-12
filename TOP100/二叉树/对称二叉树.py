"""
-*- coding: utf-8 -*-
@File  : 对称二叉树.py
@Time  : 2022/4/12
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
1,2,2,3,4,4,3
输出：
True
"""
from collections import deque
from main import list_to_binarytree


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True

        def dfs(left, right):
            # 一共有三种情况可以让递归返回
            # 左节点和右节点都等于空，返回正确
            # 左节点和右节点有一个为空，返回错误
            # 左节点和右节点不同，返回错误
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            # 上述三种情况均未发生，则证明左右节点值相同，可以进入下一层的递归比较
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root.left, root.right)


root = list_to_binarytree([1,2,2,3,4,4,3])
s = Solution()
result = s.isSymmetric(root)
print(result)
