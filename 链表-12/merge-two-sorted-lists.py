"""
-*- coding: utf-8 -*-
@File  : merge-two-sorted-lists.py
@Time  : 2022/3/18
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

合并链表的操作比较简单，关键点在于head辅助链表的加入和pre游标用链表的加入，如果没有pre无法确定当前游标进度

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node(object):
    """创建单个结点类"""

    def __init__(self, val):
        self.val = val
        self.next = None


class SingleLinkedList(object):
    """创建一个单链表"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def length(self):
        """获取链表的长度"""
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def add_fist(self, val):
        """在链表的头部添加元素"""
        node = Node(val)
        node.next = self.head
        self.head = node

    def add_last(self, val):
        """在链表的尾部添加元素"""
        node = Node(val)
        if self.is_empty():
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert_node(self, index, val):
        """在指定位置添加元素"""
        node = Node(val)
        if index < 0 or index > self.length():
            return False
        elif index == 0:
            self.add_fist()
        elif index == self.length():
            self.add_last()
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node

    def remove_node(self, val):
        """删除指定结点"""
        cur = self.head  # 指针指向的结点
        pre = None  # 指针指向结点的前一个
        if self.head == val:
            self.head.next = self.head
        else:
            while cur.data is not val:
                pre = cur
                cur = cur.next
            pre.next = cur.next

    def search_node_is_exist(self, val):
        """查找指定结点是否存在"""
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False

    def traversal(self):
        """遍历整个链表"""
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        head = ListNode(None)
        pre = head

        while list1 and list2:
            if list1.val <= list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                list2 = list2.next
            pre = pre.next

        pre.next = list1 if list1 is not None else list2

        return head.next


test_LinkedList = SingleLinkedList()
LinkedList1 = SingleLinkedList()
LinkedList2 = SingleLinkedList()
LinkedList1.add_fist(1)
LinkedList1.add_last(2)
LinkedList1.add_last(3)
LinkedList2.add_last(2)
LinkedList2.add_last(3)
LinkedList2.add_last(4)
print("操作前链表状态：")
print("l1：")
LinkedList1.traversal()
print("l2：")
LinkedList2.traversal()

removeDuplicates = Solution()
test_LinkedList.head = removeDuplicates.mergeTwoLists(LinkedList1.head, LinkedList2.head)

print("操作后链表状态：")
test_LinkedList.traversal()
