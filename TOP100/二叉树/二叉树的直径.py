"""
-*- coding: utf-8 -*-
@File  : 二叉树的直径.py
@Time  : 2022/4/16
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：利用 某一根节点的直径=左子树深度+右子树深度 ，遍历所有节点作为根节点，最终选择最大的值输出
输入：
1,2,3,4,5
输出：
3
"""


from main import list_to_binarytree

nums = input().split(",")

binary_tree = list_to_binarytree(nums)


class Solution:
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root) -> int:
        def bfs(root):
            if root is None:
                return 0
            l = bfs(root.left)
            r = bfs(root.right)
            self.max = max(self.max, l+r)
            return max(l, r) + 1
        bfs(root)
        return self.max


s = Solution()
result = s.diameterOfBinaryTree(binary_tree)
print(result)
