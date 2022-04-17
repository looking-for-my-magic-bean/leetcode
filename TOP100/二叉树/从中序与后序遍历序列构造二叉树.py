"""
-*- coding: utf-8 -*-
@File  : 从中序与后序遍历序列构造二叉树.py
@Time  : 2022/4/16
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
中序：9,3,15,20,7
后序：9,15,7,20,3
输出：
[3,9,20,null,null,15,7]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:

        def build(postleft, postright, inleft, inright):
            if postleft > postright:
                return None

            post_root = postorder[postright]
            index = inorder_dict[post_root]
            x = index - 1 - inleft + postleft

            root = TreeNode(post_root)
            root.left = build(postleft, x, inleft, index - 1)
            root.right = build(x + 1, postright - 1, index + 1, inright)

            return root

        n = len(inorder)
        inorder_dict = {}
        for i in range(n):
            inorder_dict[inorder[i]] = i
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