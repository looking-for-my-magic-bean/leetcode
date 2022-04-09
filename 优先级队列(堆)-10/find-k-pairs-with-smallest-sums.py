"""
-*- coding: utf-8 -*-
@File  : find-k-pairs-with-smallest-sums.py
@Time  : 2022/3/27
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""
import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int):

        min_heap = []
        result = []
        seen = set()
        m = len(nums1)
        n = len(nums2)
        min_heap.append((nums1[0] + nums2[0], 0, 0))
        heapq.heapify(min_heap)

        while min_heap and len(result) < k:
            _, i1, i2 = heapq.heappop(min_heap)
            result.append([nums1[i1], nums2[i2]])
            if i1 < m - 1 and (i1 + 1, i2) not in seen:
                heapq.heappush(min_heap, (nums1[i1+1] + nums2[i2], i1+1, i2))
                seen.add((i1 + 1, i2))
            if i2 < n - 1 and (i1, i2 + 1) not in seen:
                heapq.heappush(min_heap, (nums1[i1] + nums2[i2+1], i1, i2+1))
                seen.add((i1, i2 + 1))
        return result


s = Solution()
test = s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
print(test)
