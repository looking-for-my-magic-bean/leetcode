"""
-*- coding: utf-8 -*-
@File  : 从前序与中序遍历序列构造二叉树.py
@Time  : 2022/4/15
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
前序：3,9,20,15,7
后序：9,3,15,20,7
输出：
[3,9,20,null,null,15,7]
"""

from main import list_to_binarytree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:

        def build(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            preleft = preorder_left
            index = inorde_dict[preorder[preleft]]
            x = index - inorder_left + preleft

            root = TreeNode(preorder[preleft])
            root.left = build(preleft + 1, x, inorder_left, index - 1)
            root.right = build(x + 1, preorder_right, index + 1, inorder_right)
            return root

        n = len(preorder)
        inorde_dict = {}
        for i in range(n):
            inorde_dict[inorder[i]] = i
        return build(0, n - 1, 0, n - 1)


while True:
    try:
        preorder = list(map(int, input().split(",")))
        inorder = list(map(int, input().split(",")))
        s = Solution()
        result = s.buildTree(preorder, inorder)
        print(result)
    except EOFError:
        break