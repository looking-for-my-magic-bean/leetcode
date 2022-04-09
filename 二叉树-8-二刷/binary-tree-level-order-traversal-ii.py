# -*- coding: utf-8 -*-
"""
@Time: 2022/3/5 19:28
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

# 注意，list.reverse()对列表本身进行操作，不返回函数

"""
from collections import deque
from main import list_to_binarytree

binary_tree = list_to_binarytree([3,9,20,None,None,15,7])


class Solution:
    def levelOrderBottom(self, root):
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
        ans.reverse()
        return ans


test = Solution()
out = test.levelOrderBottom(binary_tree)
print(out)
