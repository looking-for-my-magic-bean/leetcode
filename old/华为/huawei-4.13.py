"""
-*- coding: utf-8 -*-
@File  : huawei-4.13.py
@Time  : 2022/4/12
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：

"""
from collections import deque
# a.sort(key=lambda x:(x[1], x[2])) # 按照二维列表的第一列排序，如果相同按照第二列排序
# [i[0] for i in ans] # 获得ans这个二维数组的第0列数值并保存到列表中
# a.insert(i, obj) # 在第i个位置插入目标obj


def func():
    n = int(input())
    s = []
    for i in range(n):
        s.append(list(map(int, input().split(","))))
    strange = list(map(int, input().split(" ")))
    result = shuchu(s, strange)
    print(" ".join(str(i) for i in result))


def shuchu(s, strange):
    ans = []
    for val in s:
        if val[1] >= strange[2] and val[2] >= strange[3] and \
                (strange[4] == 9 or strange[4] == val[3]) and (strange[5] == 2 or strange[5] == val[4]):
            # cpu优先
            if strange[1] == 1:
                ans.append(val)
                ans.sort(key=lambda x: (x[1], x[2], x[0]))
                if len(ans) > strange[0]:
                    ans.pop()
            else:
                ans.append(val)
                ans.sort(key=lambda x: (x[2], x[1], x[0]))
                if len(ans) > strange[0]:
                    ans.pop()
    ans.sort(key=lambda x: x[0])
    m = len(ans)
    result = [m] + [i[0] for i in ans]
    return result


if __name__ == "__main__":
    func()
