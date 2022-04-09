"""
-*- coding: utf-8 -*-
@File  : implement-queue-using-stacks.py
@Time  : 2022/3/24
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""


class MyQueue:

    def __init__(self):
        self.myqueue1 = []
        self.myqueue2 = []

    def push(self, x: int) -> None:
        self.myqueue1.append(x)

    def pop(self) -> int:
        if len(self.myqueue2) == 0:
            for _ in range(len(self.myqueue1)):
                self.myqueue2.append(self.myqueue1.pop())
        return self.myqueue2.pop()

    def peek(self) -> int:
        if len(self.myqueue2) == 0:
            for _ in range(len(self.myqueue1)):
                self.myqueue2.append(self.myqueue1.pop())
        return self.myqueue2[-1]

    def empty(self) -> bool:
        return len(self.myqueue1) == 0 and len(self.myqueue2) == 0


obj = MyQueue()
obj.push(3)
obj.push(4)
print('param_2', obj.pop())
print('param_3', obj.peek())
print('param_4', obj.empty())
