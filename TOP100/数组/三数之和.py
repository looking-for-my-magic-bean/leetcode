# -*- coding: utf-8 -*-
"""
@File: 三数之和.py
@Time: 2022/4/20 18:10
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：


"""


class Solution:
    def threeSum(self, nums):

        n = len(nums)
        if (not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            # 排序结果从小到大，如果第一个数就大于0则后面更大于0，相加结果一定大于0
            if (nums[i] > 0):
                return res
            # 对于重复元素直接跳过避免出现重复解
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            # 设置左右指针
            L = i + 1
            R = n - 1
            # 循环中止的条件
            while (L < R):
                # 一共会出现三种情况，左右指针对应元素与i对应元素和=0，>0，<0。
                # 等于0
                if (nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    # 防止出现重复元素
                    while (L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while (L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    # 继续寻找剩余可能结果
                    L = L + 1
                    R = R - 1
                # 大于0，说明右边界对应的数太大了，减少右边界
                elif (nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                # 小于0，说明左边界对应的数太小了，增加左边界
                else:
                    L = L + 1
        return res


ss = input()
s = Solution()
result = s.threeSum(ss)
print(result)


