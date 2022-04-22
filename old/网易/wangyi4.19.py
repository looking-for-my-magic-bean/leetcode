"""
-*- coding: utf-8 -*-
@File  : wangyi4.19.py
@Time  : 2022/4/21
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

输入：
6
7 9 5 11 2 8

输出：

"""
# def func():
#     p, q = map(int, input().split(" "))
#     # nums = list(map(int, input().split(" ")))
#     print(p, q)
#     print(1, 1)


def func():
    def iszhishu(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            return True
        else:
            return False

    def changenum(num, tar):
        ans = 0
        if num > tar:
            while True:
                num -= 1
                if iszhishu(num):
                    ans += 1
                if num == tar:
                    break
            return ans
        elif num < tar:
            while True:
                num += 1
                if iszhishu(num):
                    ans += 1
                if num == tar:
                    break
            return ans
        else:
            return 0
    n = int(input())
    nums = list(map(int, input().split(" ")))
    min_result = 9999
    for i in nums:
        result = 0
        if iszhishu(i) and i > 2:
            zhishu = i
            for val in nums:
                if val == zhishu:
                    continue
                else:
                    result += changenum(val, zhishu)
            min_result = min(result, min_result)
        else:
            continue

    print(min_result)


if __name__ == '__main__':
    func()
