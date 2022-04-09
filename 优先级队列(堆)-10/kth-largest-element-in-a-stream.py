"""
-*- coding: utf-8 -*-
@File  : kth-largest-element-in-a-stream.py
@Time  : 2022/3/26
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

堆相关操作，默认构建的是小根堆，构建大根堆可以考虑负数
heap = [] #创建了一个空堆
heappush(heap,item) #往堆中插入一条新的值
item = heappop(heap) #从堆中弹出最小值
item = heap[0] #查看堆中最小值，不弹出
heapify(x) #以线性时间讲一个列表转化为堆

item = heapreplace(heap,item) #弹出并返回最小值，然后将heapqreplace方法中item的值插入到堆中，堆的整体结构不会发生改变。
这里需要考虑到的情况就是如果弹出的值大于item的时候我们可能就需要添加条件来满足function的要求
if item > heap[0]
    item = heapreplace(heap, item)

heappushpop() #顾名思义，将值插入到堆中同时弹出堆中的最小值。
merge(*iterables) #合并多个堆然后输出
list(merge([1,3,5,7],[0,2,4,8],[5,10,15,20],[],[25]))
[0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]

nlargest(n , iterbale, key=None)
从堆中找出做大的N个数，key的作用和sorted( )方法里面的key类似，用列表元素的某个属性和函数作为关键字。
a = [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]
heapq.nlargest(5,a)
[25, 20, 15, 10, 8]
这样就返回了列表中前五个最大的数。
b = [('a',1),('b',2),('c',3),('d',4),('e',5)]
heapq.nlargest(1,b,key=lambda x:x[1])
[('e', 5)]


"""
import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.q = []
        self.size = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) > self.size:
            heapq.heappop(self.q)
        return self.q[0]


kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))
print(kthLargest.add(5))
print(kthLargest.add(10))
print(kthLargest.add(9))
print(kthLargest.add(4))
