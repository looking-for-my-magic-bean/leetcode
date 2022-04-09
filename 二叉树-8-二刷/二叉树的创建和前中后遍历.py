"""
-*- coding: utf-8 -*-
@File  : 二叉树的创建和前中后遍历.py
@Time  : 2022/4/7
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""


class Treenode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    result = []

    def qianxu(self, roots):
        if roots is None:
            return None
        self.result.append(roots.val)
        self.qianxu(roots.left)
        self.qianxu(roots.right)

    def zhongxu(self, roots):
        if roots is None:
            return None
        self.zhongxu(roots.left)
        self.result.append(roots.val)
        self.zhongxu(roots.right)

    def houxu(self, roots):
        if roots is None:
            return None
        self.houxu(roots.left)
        self.houxu(roots.right)
        self.result.append(roots.val)


def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = Treenode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root
    return level(0)


root = list_to_binarytree(["A", "B", "C", "D", None, "E", "F", "G", "H", None, None, None, "I"])
s = Solution()
# s.qianxu(root)
# s.zhongxu(root)
s.houxu(root)
print(s.result)
print("success!")
