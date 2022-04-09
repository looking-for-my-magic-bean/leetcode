"""
-*- coding: utf-8 -*-
@File  : test.py
@Time  : 2022/3/23
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""
nums = 0


class Solution:
    def change_qishui(self, num):
        ans = 0
        while num > 0:
            num_s = num // 3
            num_y = num % 3
            ans += num_s
            num = num_s + num_y
            if num == 2:
                ans = ans + 1
                return ans
            elif num == 1:
                return ans
        return None


test = Solution()
while True:
    nums = int(input())
    if nums == 0:
        break
    result = test.change_qishui(nums)
    print(result)


