"""
-*- coding: utf-8 -*-
@File  : wangyi3.py
@Time  : 2022/4/16
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：

"""
import collections


def func():
    # while True:
    #     try:
    n, k = input().split()
    n = int(n)
    k = int(k)
    s = input().split()
    ss = s[0]
    result = solution(n, k, ss)
    print(result)

        # except EOFError:
        #     break


def solution(n, k, ss):
    result = 0
    for i in range(n-1):
        if i == 0:
            for j in range(i+1, n-1):
                temp_s = ss[:i]+ss[j+1:n+1]
                # 对出现的字符串排序后还要加.most_common(2)将字典按照字母出现频率排序成列表，形式[("s",3),("a", 2)]
                temp = collections.Counter(temp_s).most_common(2)
                c = temp[0][1]
                if c <= k:
                    result += 1
        else:
            for j in range(i+1, n):
                temp_s = ss[:i]+ss[j+1:n+1]
                temp = collections.Counter(temp_s).most_common(2)
                c = temp[0][1]
                if c <= k:
                    result += 1

    return result


if __name__ == '__main__':
    func()
