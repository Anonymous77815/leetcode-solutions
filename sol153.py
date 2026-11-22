class Solution(object):
    
    def findMin(self,nums):
        
        l = 0
        r = len(nums)-1

        if nums[r]>nums[l]:
            return nums[l]

        while l<r:

            pivot = (l+r)//2

            if nums[pivot] > nums[r]:
                l = pivot

            elif nums[pivot] < nums[l]:
                r = pivot

            else:
                return nums[pivot]