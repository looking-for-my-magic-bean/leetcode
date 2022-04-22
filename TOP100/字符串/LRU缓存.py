"""
-*- coding: utf-8 -*-
@File  : LRU缓存.py
@Time  : 2022/4/21
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：

"""
# dict_demo10 = {'name': '码农飞哥', 'age': 18, 'height': 185, 'width': 100}
#
# # 删除键值对
#
# del dict_demo10['height']
#
# print('删除键height对之后的结果=', dict_demo10)
#
# # pop()方法和popitem()方法
#
# dict_demo10.pop('width')
#
# print('pop方法调用删除键width之后结果=', dict_demo10)
#
# dict_demo10 = {'name': '码农飞哥', 'age': 18, 'height': 185, 'width': 100}
#
# dict_demo10.popitem()
#
# print('popitem方法调用之后结果=', dict_demo10)
# """
# 删除键height对之后的结果= {'name': '码农飞哥', 'age': 18, 'width': 100}
# pop方法调用删除键width之后结果= {'name': '码农飞哥', 'age': 18}
# popitem方法调用之后结果= {'name': '码农飞哥', 'age': 18, 'height': 185}
# """
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.Cache_dict = {}
        self.old_report = deque([])

    def get(self, key: int) -> int:
        if key in self.Cache_dict:
            if key in self.old_report:
                self.old_report.popleft()
                self.old_report.append(key)
            else:
                self.old_report.append(key)
            return self.Cache_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.Cache_dict[key] = value
        if key in self.old_report:
            self.old_report.popleft()
            self.old_report.append(key)
        else:
            self.old_report.append(key)
        if len(self.Cache_dict) > self.capacity:
            del self.Cache_dict[self.old_report.popleft()]


lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)

