"""
-*- coding: utf-8 -*-
@File  : 前序遍历构造二叉搜索树.py
@Time  : 2022/4/17
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：抓住二叉搜索树左子树值小于根节点小于右子树的特性，将首节点取出作为根节点，将其余节点按照比根节点小，比根节点大分为左子树与右子树两部分
将左子树与右子树序列分别进行递归，最终得到二叉搜索树
输入：
8,5,1,7,10,12
输出：
[8,5,10,1,7,null,12]
"""
from main import *


class Solution:
    def bstFromPreorder(self, preorder):
        if preorder:
            p, root = [[], []], TreeNode(preorder.pop(0))
            [p[val > root.val].append(val) for val in preorder]
            root.left = self.bstFromPreorder(p[0])
            root.right = self.bstFromPreorder(p[1])
            return root


preorder = list(map(int, input().split(",")))
s = Solution()
result = s.bstFromPreorder(preorder)
print(result)
