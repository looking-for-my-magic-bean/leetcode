"""
-*- coding: utf-8 -*-
@File  : partition-list.py
@Time  : 2022/3/19
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

分隔链表的关键点在于创建两个链表，一个链表用来存小于x的，另一个链表用来存大于等于x的，注意，两个链表都需要有对应的游标！

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
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1, l2 = ListNode(), ListNode()
        cur1, cur2 = l1, l2
        cur = head
        while cur is not None:
            if cur.val >= x:
                cur2.next = cur
                cur2 = cur2.next

            else:
                cur1.next = cur
                cur1 = cur1.next
            cur = cur.next
        cur1.next = l2.next
        cur2.next = None       # 这一条必须加上，不然就会导致cur2的后面接的是原来的cur里面的元素，形成闭环的链表
        return l1.next


LinkedList = SingleLinkedList()
LinkedList.add_fist(1)
LinkedList.add_last(4)
LinkedList.add_last(3)
LinkedList.add_last(2)
LinkedList.add_last(5)
LinkedList.add_last(2)
print("操作前链表状态：")
LinkedList.traversal()

removeDuplicates = Solution()
LinkedList.head = removeDuplicates.partition(LinkedList.head, 3)

print("操作后链表状态：")
LinkedList.traversal()
