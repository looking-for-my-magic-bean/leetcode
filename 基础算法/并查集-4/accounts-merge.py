# -*- coding: utf-8 -*-
"""
@File: accounts-merge.py
@Time: 2022/4/5 12:25
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：
[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
输出：


"""


import collections


class Solution:
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [1] * n

        def find(self, x):  # 寻找x的集合节点（根节点）
            if x != self.parent[x]:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def union(self, x, y):  # 合并x,y，x与y分别代表邮箱所在的账户索引，最终让parent中x，y的位置的值对应到根节点所在的位置
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x == root_y:
                return

            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1  # 这里只在相等的时候后加了1，后续有新的元素进入并不再加一，说明这里只是防止相等无法处理的情况，并没有说谁大合并到谁那里，而是后来的合并到先前的去

    def accountsMerge(self, accounts):
        uf = Solution.UnionFind(len(accounts))
        # key: email, value: id (index)
        email_id = dict()                         # 创建email_id这个字典，键存储邮箱，值存储邮箱编号
        # key: id (index), value: email list
        id_email = collections.defaultdict(list)  # 产生一个类似dict的类，其中key是可以自己设定的，存储邮箱编号，但初始的value是可以被指定的，这里就被指定为list，存储邮箱列表

        for i, a in enumerate(accounts):  # 遍历所有账户
            for e in a[1:]:  # 遍历当前选中的账户的邮箱
                if e in email_id:  # 如果邮箱在字典内，将当前邮箱合并进字典
                    uf.union(email_id[e], i)  # 被查到相同的邮箱其键值中值为索引，代表其来自哪个账户，例如email_id[e]=0，代表来自0账户，i=1，代表来自1账户，合并
                else:
                    email_id[e] = i  # 将邮箱放入字典并保存其来自哪个账户（用i的当前值来记录，例如第一个账户时i等于0），最终字典中没有重复出现的邮箱（重复的已经被合并）

        for e, i in email_id.items():  # 遍历email_id，其键为邮箱，值为邮箱对应的账户索引
            id_email[uf.find(i)].append(e)  # 注意这里id_email的key 将i的根节点的位置作为键，值为对应邮箱的列表

        return [[accounts[i][0]] + sorted(e) for i, e in id_email.items()]  # 遍历id_email，取其键（存储根账户的索引）作为索引，值（存储邮箱的列表）作为邮箱列表并排序与头对接


s = Solution()
# test = s.accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
#                         ["Mary", "mary@mail.com"], ["John",  "johnsmith@mail.com", "johnnybravo@mail.com"]])
test = s.accountsMerge([["John", "A", "B", "C"],
                        ["John", "A", "S", "Z"],
                        ["John", "A", "M", "N"],
                        ["John", "D", "E", "F"],
                        ["John",  "F", "H"],
                        ["John",  "B", "H"]])
print(test)
