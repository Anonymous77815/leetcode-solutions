class Solution(object):
    def productExceptSelf(self, nums):

        n = len(nums)
        result = []

        i = 0
        j = 0
        productArr = 1

        while j < n:

            if i == n:
                result.append(productArr)
                j += 1
                i = 0
                productArr = 1
                continue

            if i == j:
                i += 1
                continue

            productArr *= nums[i]
            i += 1

        return result