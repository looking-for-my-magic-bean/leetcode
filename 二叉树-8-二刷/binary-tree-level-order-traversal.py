# -*- coding: utf-8 -*-
"""
@Time: 2022/3/5 19:28
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

关键点在于q里面存放的是节点而不是节点的值，要先把节点拿出来！！！

"""
from collections import deque
from main import list_to_binarytree

binary_tree = list_to_binarytree([3, 9, 20, None, None, 15, 7])


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            n = len(q)
            t = []
            for _ in range(n):
                node = q.popleft()
                t.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(t)
        return ans


test = Solution()
out = test.levelOrder(binary_tree)
print(out)
