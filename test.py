from distutils.log import error


class Solution(object):
    def twoSum(self, nums, target):

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def Listinsert(self, L, i, e):
        if (i<1 | i>len(L)):
            return error
        if (i<= len(L)):
            for k in range(len(L)-1, i-1, -1):
                L[k+1] = L[k]
        L[i-1] = e
        return L


list_test = [1,2,3,4,5,6,7,]
result = Solution()
print(result.Listinsert(list_test,3,666))