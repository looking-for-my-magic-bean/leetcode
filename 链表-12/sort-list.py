"""
-*- coding: utf-8 -*-
@File  : sort-list.py
@Time  : 2022/3/19
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

链表排序的关键除去最前面的递归退出判断外主要分为三大项：
1、快慢针找到链表中点，分为左右链表
2、递归
3、递归内部的操作，比如比较链表值并加入到辅助链表中

"""

from main import ListNode
from main import SingleLinkedList


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 二分法最终保证分到最小单位了
        if head is None or head.next is None:
            return head
        # 产生快慢指针，用于找到链表的中点
        slow, fast = head, head.next
        # 快慢指针找中点的核心代码
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        t = slow.next
        slow.next = None           # 注意，一定要记得将慢链表的末尾指向清楚（赋值为None）
        # 递归法
        l1 = self.sortList(head)
        l2 = self.sortList(t)
        # 递归后将拿到的值进行比对并放入辅助链表中
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        # 返回当前递归排序后的结果
        return dummy.next


LinkedList = SingleLinkedList()
LinkedList.add_fist(4)
LinkedList.add_last(2)
LinkedList.add_last(1)
LinkedList.add_last(3)
print("操作前链表状态：")
LinkedList.traversal()

removeDuplicates = Solution()
LinkedList.head = removeDuplicates.sortList(LinkedList.head)

print("操作后链表状态：")
LinkedList.traversal()
