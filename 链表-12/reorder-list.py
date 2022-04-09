"""
-*- coding: utf-8 -*-
@File  : reorder-list.py
@Time  : 2022/3/19
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

链表重拍是一个非常综合性的题目，其包含了
1、快慢指针找中点
2、反转链表
3、合并链表
这个题做会了，相当于会了三个点

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
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        # 快慢指针找到中点，分成前后两段链表
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        cur = slow.next
        slow.next = None

        # 将后半段链表反转
        start = cur
        while start.next:
            tmp = start.next
            start.next = start.next.next
            tmp.next = cur
            cur = tmp
        # 将前后两段链表合并
        left, right = head, cur
        while right:
            t = right.next
            right.next = left.next
            left.next = right
            left = right.next
            right = t


LinkedList = SingleLinkedList()
LinkedList.add_fist(1)
LinkedList.add_last(2)
LinkedList.add_last(3)
LinkedList.add_last(4)
print("操作前链表状态：")
LinkedList.traversal()

removeDuplicates = Solution()
removeDuplicates.reorderList(LinkedList.head)
print("操作后链表状态：")
LinkedList.traversal()
