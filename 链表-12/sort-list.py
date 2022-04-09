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
