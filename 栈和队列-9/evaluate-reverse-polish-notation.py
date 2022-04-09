"""
-*- coding: utf-8 -*-
@File  : evaluate-reverse-polish-notation.py
@Time  : 2022/3/21
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm

逆波兰表达式求值的关键点在于用栈可以很好的解决
1、遍历tokens列表中的值
2、如果token值为（+，-，*，/）则将栈中的两个数弹出来进行运算并再压入栈
3、如果是数值就直接压入栈
4、最后返回链表的[0]值

"""


class Solution:
    def evalRPN(self, tokens):
        def compo(num1, op, num2):  # num1为栈底数，num2为栈顶数
            if op == '+':
                return num1 + num2
            elif op == '-':
                return num1 - num2
            elif op == '*':
                return num1 * num2
            elif op == '/':
                result = abs(num1) // abs(num2)
                return result if num1 * num2 > 0 else -result

        stack = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append((compo(num1, token, num2)))
            else:
                stack.append(int(token))

        return stack[0]


test = ["2", "1", "+", "3", "*"]
nibolan = Solution()
result = nibolan.evalRPN(test)
print('result:', result)
