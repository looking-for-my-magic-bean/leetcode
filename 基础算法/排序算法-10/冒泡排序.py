"""
@Time: 2022/3/13 13:23
@Author: TK <TK@bupt.edu.cn>
@Software: PyCharm

比较前后两数的大小，小的往前，大的往后。
关键点在于如何循环遍历，这里用两个for循环，j用来比较前后两个数，i用来确定还有多少需要去比较，i越大，后面的数确定的越多，需要去比较的数越少。

"""


class Solution:
    def bubbleSort(self, nums):
        nums_len = len(nums)
        for i in range(nums_len-1):         # 这里i的范围如果是到nums_len的话j的最后一轮遍历就是for j in range(0),没有意义。
            for j in range(nums_len-1-i):
                if nums[j] > nums[j+1]:
                    temp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = temp
        return nums


test_list = [1,4,2,0]
test = Solution()
result = test.bubbleSort(test_list)
print(result)
