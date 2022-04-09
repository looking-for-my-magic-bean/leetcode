"""
-*- coding: utf-8 -*-
@File  : 插入排序.py
@Time  : 2022/3/13
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

插入排序的根本在于从前往后遍历每一个变量，寻找其前方比自己大的数值让其往后移动并插入在其前方。

"""


# class Solution:
#     def Insertion_Sort(self, nums):
#         nums_len = len(nums)
#         for i in range(1, len(nums)):
#             preindex = i - 1
#             current = nums[i]
#             while preindex >= 0 and current < nums[preindex]:
#                 nums[preindex + 1] = nums[preindex]
#                 preindex -= 1
#             nums[preindex + 1] = current
#         return nums


test_list = [1,4,2,0]
test = Solution()
result = test.Insertion_Sort(test_list)
print(result)
