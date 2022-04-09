"""
-*- coding: utf-8 -*-
@File  : 堆排序.py
@Time  : 2022/3/27
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""
import heapq


# class Solution:
#
#     def sort(self, nums):
#
#         result = []
#         heapq.heapify(nums)
#
#         for i in range(len(nums)):
#             result.append(heapq.heappop(nums))
#
#         return result

class Solution:
    def heap_adjust(self, A, start=0, end=None):
        if end is None:
            end = len(A)

        while start is not None and start < end // 2:  # start < end // 2是为了判断该节点是不是树的叶子节点
            l, r = start * 2 + 1, start * 2 + 2
            swap = None

            if A[l] > A[start]:
                swap = l
            if r < end and A[r] > A[start] and (swap is None or A[r] > A[l]):
                # r < end为了消除最后一个节点的影响，后面用来判断右节点大于开始点且大于左节点
                swap = r

            if swap is not None:
                A[start], A[swap] = A[swap], A[start]  # 注意：这种同时赋值最终结果是与分开赋值不同，能达到交换数组元素的目的

            start = swap
            # 不发生交换start为None，发生交换后start不满足< end // 2，两种情况下都退出，只有交换后还不是叶节点的时候才继续进行交换

        return

    def heapsort(self, A):

        # construct max heap
        n = len(A)
        for i in range(n // 2 - 1, -1, -1):
            # 从底部开始寻找子树的顶点，然后向上移动，针对未曾排序过的堆用，先右子树排序，再左子树，再根节点，需要调整多次
            # 因为这个堆未曾排过序，从顶点开始会出现顶点落入一边子树，另一边子树未排序的状况。
            self.heap_adjust(A, i)
        # self.heap_adjust(A)

        # sort
        for i in range(n - 1, 0, -1):
            # 对交换顶点和最后一个点并且去掉最后一个点的堆进行整理为最大堆，这时直接设置start从根节点开始，让根节点不断下沉，只需调用一次调整
            # 因为这时另一边的子树已经拍好序了
            A[0], A[i] = A[i], A[0]
            self.heap_adjust(A, end=i)

        return A


# test_list = [7, 6, 8, 5, 2, 1, 3]
test_list = [7, 6, 8, 5, 2, 1, 3, 4, 0, 9, 10]
test = Solution()
result = test.heapsort(test_list)
# test.heap_adjust(test_list)
print(result)


