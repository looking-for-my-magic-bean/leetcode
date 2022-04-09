"""
-*- coding: utf-8 -*-
@File  : palindrome-linked-list.py
@Time  : 2022/3/20
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

回文链表的思路：
1、快慢指针找中点
2、后续链表反转
3、遍历后续链表与前链表比较
注意：12021这种链表也是回文链表，因此在第三部遍历的是后续链表，遍历完就可以认为是回文了，因为中间的零无需遍历。

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
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        tmp = slow.next
        slow.next = None

        start = tmp
        while start.next is not None:
            cur = start.next
            start.next = start.next.next
            cur.next = tmp
            tmp = cur

        l1, l2 = head, tmp
        while l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True


LinkedList = SingleLinkedList()
LinkedList.add_fist(1)
LinkedList.add_last(0)
LinkedList.add_last(1)
print("操作前链表状态：")
LinkedList.traversal()

removeDuplicates = Solution()
result = removeDuplicates.isPalindrome(LinkedList.head)

print("操作后链表状态：")
print(result)
