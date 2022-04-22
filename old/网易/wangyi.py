"""
-*- coding: utf-8 -*-
@File  : wangyi4.19.py
@Time  : 2022/4/16
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：

"""


def func():
    # while True:
    #     try:
    m, n = input().split()
    m = int(m)
    n = int(n)
    ss = []
    for i in range(m):
        s = input().split()
        a = []
        for j in s[0]:
            a.append(j)
        ss.append(a)
    result = solution(m, n, ss)
    print(result)

        # except EOFError:
        #     break


def solution(m, n, ss):
    result = 0
    ss_temp = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            # 保证位置为*且没可能被占领
            if ss[i][j] == "*" and ss_temp[i][j] == 0:
                result += 1
                # 向上下左右去寻找可以被占领的位置，如果可以被占领，左上的已经找过它了，只需要向右下找
                for x in range(i, m, 2):
                    for y in range(j, n, 2):
                        # 确保下一跳不会进湖里
                        if ss[x][y] != ".":
                            if ss_temp[x][y] == 0:
                                ss_temp[x][y] = 1
                        else:
                            break
    return result


if __name__ == '__main__':
    func()

