"""
-*- coding: utf-8 -*-
@File  : huawei-4.6.py
@Time  : 2022/4/6
@Author: Tk <TK@bupt.edu.cn>
@Software: PyCharm



"""
import collections

n, m = map(int, input().split(" "))
# title = []
# text = []
# for i in range(m * 2):
#     if i % 2 == 0:
#         title += input().split(" ")
#     else:
#         text += input().split(" ")

title = ['xinguan', 'feiyan', 'xinzeng', 'bendi', 'quezhen', 'anli', 'xinguan', 'yimiao', 'linchuang', 'shiyan']
text = ['ju', 'baodao', 'chengdu', 'xinzeng', 'xinguan', 'feiyan', 'bendi', 'quezhen', 'anli', 'yili', 'shenzhen',
        'xinzeng', 'bendi', 'quezhen', 'anli', 'liangli', 'yiqing', 'zhengti', 'kongzhi', 'lianghao', 'wuzhong',
        'xinguan', 'yimiao', 'tongguo', 'sanqi', 'linchuang', 'shiyan', 'xiaoguo', 'lianghao']


class Solution:
    def find_hot_word(self, ti, te, n):
        all_result = ""
        ti = ti * 3
        result = ti + te
        re_dict = collections.Counter(result)
        print(re_dict)
        for i, (key, value) in enumerate(re_dict.most_common(n)):
            all_result += (key + " ")
        all_result = all_result[:-1]
        return all_result


s = Solution()
test = s.find_hot_word(title, text, n)
print(test)



