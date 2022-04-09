"""
-*- coding: utf-8 -*-
@File  : 选择排序.py
@Time  : 2022/3/13
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

分为已排序列和未排序列，将未排序列中的最小值添加到已排序列末尾。
注意，冒牌算法是大的沉到下面，所以后面的无需再拍，选择排序是小的放到前面，所以前面无需再排。

"""


class Solution:
    def Selection_Sort(self, nums):
        nums_len = len(nums)
        for i in range(nums_len):
            min_index = i
            for j in range(i + 1, nums_len):  # 从i的下一位开始找，因为i一开始被认为是最小的
                if nums[j] < nums[min_index]:
                    min_index = j
            temp = nums[i]
            nums[i] = nums[min_index]
            nums[min_index] = temp
        return nums


test_list = [1,4,2,0]
test = Solution()
result = test.Selection_Sort(test_list)
print(result)
