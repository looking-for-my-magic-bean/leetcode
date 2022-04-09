"""
-*- coding: utf-8 -*-
@File  : kth-smallest-element-in-a-sorted-matrix.py
@Time  : 2022/3/27
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""
import heapq


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:

        N = len(matrix)

        min_heap = []
        for i in range(min(k, N)):  # 这里用了一点列有序的性质，第k个最小只可能在前k行中(k行以后的数至少大于了k个数)
            min_heap.append((matrix[i][0], i, 0))

        heapq.heapify(min_heap)

        while k > 0:
            num, r, c = heapq.heappop(min_heap)

            if c < N - 1:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

            k -= 1

        return num


s = Solution()
test = s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
print(test)

