# -*- coding: utf-8 -*-
"""
@Time: 2022/3/4 23:09
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

注意是锯齿形遍历而不是顺序层序遍历！
flag_reverse = not flag_reverse是个很好的Ture/False写法
"""
from collections import deque
from main import list_to_binarytree

binary_tree = list_to_binarytree([3, 9, 20, None, None, 15, 7])


class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        left, ans = False, []
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
            if left:
                t.reverse()
            left = not left
            ans.append(t)
        return ans


test = Solution()
out = test.levelOrder(binary_tree)
print(out)

