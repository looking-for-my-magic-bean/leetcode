# -*- coding: utf-8 -*-
"""
@File: 两数相加.py
@Time: 2022/4/19 15:22
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm
核心思想：这个题本身不难，重点在于链表的建立和遍历。
输入：
2,4,3
5,6,4
输出：
[7,0,8]
"""
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        node_list = []
        flag = 0
        while l1 and l2:
            node_list.append((l1.val + l2.val + flag) % 10)
            flag = (l1.val + l2.val + flag)//10
            l1 = l1.next
            l2 = l2.next
        while l1:
            node_list.append((l1.val + flag) % 10)
            flag = (l1.val + flag)//10
            l1 = l1.next
        while l2:
            node_list.append((l2.val + flag) % 10)
            flag = (l2.val + flag)//10
            l2 = l2.next
        if flag:
            node_list.append(flag)
        root = ListNode(node_list[0])
        head = root
        for i in node_list[1:]:
            root.next = ListNode(i)
            root = root.next
        return head


l1 = list(map(int, input().split(",")))
l2 = list(map(int, input().split(",")))
root1 = ListNode(l1[0])
head_l1 = root1
for i in l1[1:]:
    root1.next = ListNode(i)
    root1 = root1.next

root2 = ListNode(l2[0])
head_l2 = root2
for i in l2[1:]:
    root2.next = ListNode(i)
    root2 = root2.next
s = Solution()
result = s.addTwoNumbers(head_l1, head_l2)
print(result)
