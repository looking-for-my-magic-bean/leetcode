"""
-*- coding: utf-8 -*-
@File  : remove-duplicates-from-sorted-list-ii.py
@Time  : 2022/3/18
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

删除重复元素的所有节点的关键点在于假(辅助)链表的创立，通过多一位的辅助链表可以实现cur的前移，将相同数值的节点全部删除

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
    def deleteDuplicates(self, head):
        dummy = ListNode(-1, head)  # 添加一个假的辅助链表，比正常链表长一位
        cur = dummy
        while cur.next and cur.next.next:   # 这里一定要加cur.next的判断，因为[-1,1,1]这种删完后cur没有两个next
            if cur.next.val == cur.next.next.val:  # 比较cur的后一个和后后一个
                val = cur.next.val                 # 一旦相等保存这个值，后续需要用到
                while cur.next and cur.next.val == val:  # 后面等于这个值的所有next节点全部删除
                    cur.next = cur.next.next
            else:                                  # 没有就常规后移
                cur = cur.next
        return dummy.next                          # 返回正常的


LinkedList = SingleLinkedList()
LinkedList.add_fist(1)
LinkedList.add_last(1)
LinkedList.add_last(1)
LinkedList.add_last(2)
LinkedList.add_last(3)
LinkedList.add_last(4)
print("操作前链表状态：")
LinkedList.traversal()

removeDuplicates = Solution()
LinkedList.head = removeDuplicates.deleteDuplicates(LinkedList.head)

print("操作后链表状态：")
LinkedList.traversal()
