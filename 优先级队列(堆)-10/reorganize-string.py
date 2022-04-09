"""
-*- coding: utf-8 -*-
@File  : reorganize-string.py
@Time  : 2022/3/28
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""
import collections
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:

        max_dup = (len(S) + 1) // 2
        counts = collections.Counter(S)  # 这个函数可以统计字符串中所有字符的出现频率并储存为字典

        heap = []
        for key, val in counts.items():  # 按照出现频率的高低遍历取每个元素的键值对
            if val > max_dup:  # 如果某一个元素出现的频率大于一半了，说明不能排序，直接返回“ ”
                return ''
            heap.append([-val, key])  # 给val加负号是为了将最小堆转换为最大堆
        heapq.heapify(heap)

        result = []
        while len(heap) > 1:  # 设置大于1而不是大于0是因为如果是偶数，则刚好最后还有两个元素，一起用掉，如果是奇数则剩下一个单独处理
            # 保持前端为最高频的两个字符串
            first = heapq.heappop(heap)
            result.append(first[1])
            first[0] += 1
            second = heapq.heappop(heap)
            result.append(second[1])
            second[0] += 1

            if first[0] < 0:
                heapq.heappush(heap, first)
            if second[0] < 0:
                heapq.heappush(heap, second)

        if len(heap) == 1:  # 用于是奇数时单独处理
            result.append(heap[0][1])

        return ''.join(result)   # str.join(list)用字符串str连接list中的元素


s = Solution()
test = s.reorganizeString("abbcaabca")
# test = s.reorganizeString(["ab", "df", "aaa", "ab"])
print(test)
