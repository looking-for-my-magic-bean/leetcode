# -*- coding: utf-8 -*-
"""
@File: 有效的括号.py
@Time: 2022/4/9 16:46
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

输入：
"()[]{}"
输出：
True

"""
ss = "()[]{}"


class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        s_dict = {"(":")", "{":"}", "[":"]"}
        for val in s:
            if len(ans) == 0:
                ans.append(val)
            else:
                temp = ans.pop()
                if temp in s_dict:
                    if s_dict[temp] == val:
                        pass
                    else:
                        ans.append(temp)
                        ans.append(val)
                else:
                    return False
        if len(ans) == 0:
            return True
        else:
            return False


s = Solution()
result = s.isValid(ss)
print(result)
