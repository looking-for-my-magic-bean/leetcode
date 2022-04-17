"""
-*- coding: utf-8 -*-
@File  : huawei-4.13.py
@Time  : 2022/3/30
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：板卡芯片数量 M，1~32
     用户业务配置数量 N，1~128
     用户业务配置与业务配置间用空格分隔
输出：芯片编号
     芯片资源ID

"""


M = int(input())
N = 6
server = input().split(" ")

# M = 3
# N = 6
# server = ['A','B','A','B','A','A']
# server = ['A','A','A','A','A','A']


class Solution:
    def ro(self, m, n, servers):

        m_id = 0
        flag = 0
        first = 0
        server_id = 0
        if "A" in server:  # 判断A是否在列表里
            m_id = 1
            flag = 1
        for val in server:  # 遍历列表
            if val == 'A':  # 业务A
                if first == 0:
                    flag = m_id
                    first += 1
                if server_id >= 4:
                    flag = m_id + 1
                    m_id += 1
                    server_id = 0
                server_id += 1
            else:           # 业务B
                m_id += 1

        if m_id > m:  # 芯片数量不够了
            m_id = 0
            server_id = 0
        else:
            if server[-1] == "A":
                m_id = flag
            else:
                server_id = 4

        return m_id, server_id

#
# s = Solution()
# num, server_id = s.ro(M, N, server)
# print(num, server_id)









