"""
-*- coding: utf-8 -*-
@File  : decode-string.py
@Time  : 2022/3/22
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

解码字符串主要分为四部分：
1、数字如何处理？ 尤其是多位数字情况下
2、[ 怎么处理？ 代表数字已经完事，可以压入栈中，res也要压入栈中（因为可能是第二次出现[了），清空num和res
3、] 怎么处理？ 代表字符串已经读取完毕，将原栈中字符串与当前字符串的倍数相加合并，得到新的字符串
4、字符串怎么处理？ 利用res += c来实现字符串的累加

"""


class Solution:
    def decodeString(self, s: str) -> str:
        s1, s2 = [], []
        num, res = 0, ''
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)  # num*10 是为了数字为两位数时，连续读取到两个数字，能够将大于十的数字读出来（无论几位数都可用!）
            elif c == '[':
                s1.append(num)
                s2.append(res)
                num, res = 0, ''  # 清空num和res，准备往res中填入新的字符串
            elif c == ']':
                res = s2.pop() + res * s1.pop()  # 核心处理：将存储字符串的栈顶自负串拿出来进行合并（注意整个字符串算一个元素）
            else:
                res += c  # 增加字符串
        return res


test_str = "3[ak]2[bc]"
decodestr = Solution()
result = decodestr.decodeString(test_str)
print('result', result)
