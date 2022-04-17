"""
-*- coding: utf-8 -*-
@File  : 合并二叉树.py
@Time  : 2022/4/16
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

核心思想：将root2的值合并到root1上
关键点：root1和root2为空时如何处理
输入：
1,3,2,5
2,1,3,null,4,null,7
输出：
[3,4,5,5,4,null,7]
"""
from main import list_to_binarytree

nums1 = input().split(",")
nums2 = input().split(",")
nums1 = [int(i) if i != "null" else None for i in nums1]
nums2 = [int(i) if i != "null" else None for i in nums2]
binary_tree1 = list_to_binarytree(nums1)
binary_tree2 = list_to_binarytree(nums2)


class Solution:
    def mergeTrees(self, root1, root2):
        def dfs(root1, root2):
            if (root1 is None) or (root2 is None):
                return root1 if root1 else root2
            root1.val = root1.val + root2.val
            root1.left = dfs(root1.left, root2.left)
            root1.right = dfs(root1.right, root2.right)
            return root1
        return dfs(root1, root2)


s = Solution()
result = s.mergeTrees(binary_tree1, binary_tree2)
print(result)
