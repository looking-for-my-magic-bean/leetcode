# -*- coding: utf-8 -*-
"""
@Time: 2022/3/4 23:09
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

观察题目，发现中序遍历最符合从左到右依次增大的特性，用中序遍历的方法比较前后大小实现代码。
"""
from collections import deque
from main import list_to_binarytree

binary_tree = list_to_binarytree([5,1,6,None,None,3,7])


class Solution:
    def isValidBST(self, root):
        def dfs(root):
            nonlocal prev  # 本地变量，在函数内部声明，在函数外部赋值。
            if root is None:
                return True
            if not dfs(root.left):
                return False
            if prev >= root.val:
                return False
            prev = root.val
            if not dfs(root.right):
                return False
            return True

        prev = float('-inf')  # 负无穷
        return dfs(root)


test = Solution()
out = test.isValidBST(binary_tree)
print(out)

