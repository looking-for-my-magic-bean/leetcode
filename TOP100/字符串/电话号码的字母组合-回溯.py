# -*- coding: utf-8 -*-
"""
@File: 电话号码的字母组合-回溯.py
@Time: 2022/5/3 14:12
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：

输出：


"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mon", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        n = len(digits)
        res = []
        def huisu(depth, path):
            if depth == n:
                res.append("".join(path.copy()))
            else:
                digit = digits[depth]
                for val in num_dict[digit]:
                    path.append(val)
                    huisu(depth+1, path)
                    path.pop()
        huisu(0, [])
        return res


nums = "234"
solution = Solution()
res = solution.letterCombinations(nums)
print(res)

