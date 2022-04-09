"""
-*- coding: utf-8 -*-
@File  : min-stack.py
@Time  : 2022/3/21
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

栈的基本操作有三个：
1、push 一般通过append来加入列表
2、pop  一般通过.pop()来操作
3、top  一般通过返回list[-1]来操作

"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.mins = [float('inf')]

    def push(self, val: int):
        self.s.append(val)
        self.mins.append(min(self.mins[-1], val))

    def pop(self):
        self.s.pop()
        self.mins.pop()  # 为什么min列表也要同时移除？因为后续来了小的，小数再上，但原栈删除后，小数也要跟着删除

    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.mins[-1]


obj = MinStack()
obj.push(3)
obj.push(2)
obj.push(4)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print('obj.top:', param_3)
print('obj.getMin:', param_4)
