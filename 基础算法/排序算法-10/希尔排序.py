"""
-*- coding: utf-8 -*-
@File  : 希尔排序.py
@Time  : 2022/3/13
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

希尔排序是在插入排序算法的基础上进行了进一步的改进的算法，关键点在于步长的选择。
插入排序算法可以看做是初始步长选择为 1 的希尔算法。

"""


class Solution:
    def Shell_Sort(self, nums):
        nums_len = len(nums)
        step = nums_len // 2                                      # 希尔算法特有的步长
        # step = 1  这时就是正常的插入排序
        while step > 0:                                           # 希尔算法特有的步长判断，最终步长等于1（相当于正常插入算法）
            for i in range(step, len(nums)):
                preindex = i - step
                current = nums[i]
                while preindex >= 0 and current < nums[preindex]:
                    nums[preindex + step] = nums[preindex]
                    preindex -= step
                nums[preindex + step] = current
            step //= 2                                            # 调整步长以满足不同步长情况下实现插入排序
        return nums


test_list = [1,4,2,0,3,7,9,1,3]
test = Solution()
result = test.Shell_Sort(test_list)
print(result)
