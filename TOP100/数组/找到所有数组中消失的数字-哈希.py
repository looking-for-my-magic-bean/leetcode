"""
-*- coding: utf-8 -*-
@File  : 找到所有数组中消失的数字-哈希.py
@Time  : 2022/4/10
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：

"""
nums = [4,3,2,7,8,2,3,1]


# # 哈希-复杂度为o(n)
# class Solution:
#     def findDisappearedNumbers(self, nums):
#         n = len(nums)
#         result = []
#         nums_dict = {}
#         for num in nums:
#             nums_dict[num] = ""
#
#         for i in range(1, n+1, 1):
#             if i in nums_dict:
#                 pass
#             else:
#                 result.append(i)
#         return result


# 哈希-复杂度为o(n)
class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        result = []
        for num in nums:
            x = (num - 1) % n  # 如果没有对n取余的话，在前边的数更改了后边的数的大小后无法确定后边数的原来值
            nums[x] += n

        for i in range(n):
            if nums[i] > n:
                pass
            else:
                result.append(i+1)
        return result


s = Solution()
result = s.findDisappearedNumbers(nums)
print(result)
