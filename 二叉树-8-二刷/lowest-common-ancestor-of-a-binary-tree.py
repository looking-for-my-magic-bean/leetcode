# -*- coding: utf-8 -*-
"""
@Time: 2022/3/4 23:15
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm
"""
from main import list_to_binarytree

binary_tree = list_to_binarytree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
p = 7
q = 8


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root.val == p or root.val == q:  # 注意leetcode里面是以节点的形式呈现的，所以leetcode是root == p or root == q
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # 左右两边都为空的情况下代表这个节点下没有p，q，返回空值，若找到p，q，则返回是p，q的节点
        if left is None:   # 一边为空的时候另一边一定为祖先。（因为是另一边的根）
            return right
        if right is None:
            return left
        return root  # 只有当两边都不为空时才返回该root节点，代表其是根节点


test = Solution()
out = test.lowestCommonAncestor(binary_tree, p, q)
print(out.val)
