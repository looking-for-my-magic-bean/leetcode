"""
-*- coding: utf-8 -*-
@File  : 归并排序.py
@Time  : 2022/3/13
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

归并排序的核心是利用了递归算法，分到每一个小组去排序，排好序的小组再与上层小于去比较排序，时间复杂度始终为 O(nlogn)

"""


class Solution:
    def merge(self, A, B):
        C = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] >= B[j]:
                C.append(B[j])
                j += 1
            else:
                C.append(A[i])
                i += 1
        if i < len(A):   # 这个判断的目的是为了防止当上面循环完成后还有一边的数组内容没能加到C中去
            C += A[i:]   # 此处要带:，不然A[i]是一个常数，不能与数组相加,并且此处要用c=c+a的形式，直接append后面加的是个数组[1,2,[a]]
        if j < len(B):
            C += B[j:]
        return C

    def Merge_Sort(self, nums):
        nums_len = len(nums)
        if nums_len < 2:
            return nums[:]
        left = self.Merge_Sort(nums[:nums_len//2])
        right = self.Merge_Sort(nums[nums_len//2:])

        return self.merge(left, right)


test_list = a = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
test = Solution()
result = test.Merge_Sort(test_list)
print(result)

