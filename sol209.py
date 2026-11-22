class Solution(object):
    def minSubArrayLen(self, target, nums):

        left = 0
        sumWindow = 0
        minArr = []

        for right in range(len(nums)):

            sumWindow = sumWindow + nums[right]

            while sumWindow >= target:

                minArr.append(right - left + 1)

                sumWindow = sumWindow - nums[left]

                left = left + 1

        if not minArr:
            return 0

        return min(minArr)