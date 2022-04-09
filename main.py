# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 其实是以层序遍历加递归的方式去添加元素，核心点在于2 * index + 1与2 * index + 2分别代表了当前index的左右两个子树的根节点位置
def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = TreeNode(nums[index])
        root.left = level(2 * index + 1)
        root.right = level(2 * index + 2)
        return root

    return level(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    binary_tree = list_to_binarytree([3, 9, 20, None, None, 15, 7])
    print("Great!")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
