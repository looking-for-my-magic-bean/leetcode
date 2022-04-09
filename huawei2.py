"""
-*- coding: utf-8 -*-
@File  : huawei2.py
@Time  : 2022/3/30
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""


# n = int(input())
# ss = []
# while n > 0:
#     n -= 1
#     s = int(input())
#     ss.append(s)
# result = list(set(ss))
# result.sort()
# for i in result:
#     print(i)
n = 1
s = []
while n > 0:
    try:
        n -= 1
        # s.append(input().replace('0x', ''))
        s.append(input())
    except:
        break
for val in s:
    print(int(val, 16))


