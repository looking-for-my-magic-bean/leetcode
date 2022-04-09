"""
-*- coding: utf-8 -*-
@File  : meeting-rooms-ii.py
@Time  : 2022/3/28
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

注意：sort()函数用法
# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序
random.sort(key=takeSecond) # 这里key的值是一个函数

"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals) -> int:

        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda item: item[0])  # 按照第一位元素排序
        end_times = [intervals[0][1]]  # 将排序列表中的第一个元素的结束时间赋值给end_times

        for interval in intervals[1:]:  # 遍历第一个元素以后的元素
            if end_times[0] <= interval[0]:  # 如果后来的元素的开始时间大于当前最小的结束时间，则将当前最小的结束时间弹出
                heapq.heappop(end_times)

            heapq.heappush(end_times, interval[1])  # 更新结束时间的堆，保证后来的元素的结束时间在堆中

        return len(end_times)


s = Solution()
test = s.minMeetingRooms([[0,30],[5,10],[15,20],[6,14]])
print(test)
