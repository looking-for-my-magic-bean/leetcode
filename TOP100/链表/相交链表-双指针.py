"""
-*- coding: utf-8 -*-
@File  : 相交链表-双指针.py
@Time  : 2022/4/12
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
8
[4,1,8,4,5]
[5,6,1,8,4,5]
2
3
输出：
Intersected at '8'

"""
from main import ListNode
from main import SingleLinkedList


class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = headB if pA == None else pA.next
            pB = headA if pB == None else pB.next
        return pA


LinkedList = SingleLinkedList()
LinkedList.add_fist(4)
LinkedList.add_last(2)
LinkedList.add_last(1)
LinkedList.add_last(3)
print("操作前链表状态：")
LinkedList.traversal()

removeDuplicates = Solution()