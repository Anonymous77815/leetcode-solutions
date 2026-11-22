class Solution(object):
    def findPeakElement(self, nums):

        low = 0
        high = len(nums)-1

        while low<high:

            mid = (high+low)//2

            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:

                return nums[mid]

            elif nums[mid] > nums[mid+1]:

                high = mid

            elif nums[mid] < nums[mid+1]:

                low = mid+1


        return nums[low]