# -*- coding: utf-8 -*-
"""
@Time: 2022/3/6 17:05
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm
该方法是最基础的方法，目标是在树的最底端也就是叶节点处进行插入，只要通过二叉搜索树的特性进行左小右大的比较即可定位插入位置，最终返回的是插入节点后的子树，TreeNode(val)代表创建一个子树。
"""
from main import list_to_binarytree

binary_tree = list_to_binarytree([10,5,17,1,6])


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root, val: int):
        def dfs(root):
            if root is None:                   # 如果最后遍历到了None，代表遍历到了这个子树的低端，并且根据前面的判断，可以在此位置插入该元素
                return TreeNode(val)
            if root.val < val:                 # 二叉搜索树的特性是左小右大，充分利用该特性进行数值的比较，插入的数值比根节点大往右找，反之往左找
                root.right = dfs(root.right)
            else:
                root.left = dfs(root.left)
            return root

        return dfs(root)


test = Solution()
out = test.insertIntoBST(binary_tree, 7)
print(out)

