"""
-*- coding: utf-8 -*-
@File  : binary-tree-inorder-traversal.py
@Time  : 2022/3/22
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

中序遍历二叉树：
1、递归遍历
2、栈实现非递归

"""
from main import list_to_binarytree

binary_tree = list_to_binarytree([3, 9, 20, None, None, 15, 7])


class Solution:
    # 递归遍历
    def inorderTraversal_recursion(self, root):

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        ans = []
        dfs(root)
        return ans
    # 栈实现非递归
    def inorderTraversal_unrecursion(self, root):
        ans, stk = [], []
        while root or stk:
            if root:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                ans.append(root.val)
                root = root.right
        return ans


test = Solution()
result_recursion = test.inorderTraversal_recursion(binary_tree)
result_unrecursion = test.inorderTraversal_unrecursion(binary_tree)
print(result_recursion)
print(result_unrecursion)

