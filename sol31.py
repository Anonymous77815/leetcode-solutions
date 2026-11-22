class Solution(object):
    def nextPermutation(self, nums):

        if len(nums) == 1:
            return nums

 
        if nums[::-1] == sorted(nums):
            nums.sort()
            return nums

        
        if nums[len(nums)-2] < nums[len(nums)-1]:

                nums[len(nums)-2], nums[len(nums)-1] = nums[len(nums)-1], nums[len(nums)-2]

                return nums

        j = len(nums)-1
        numsSorted = sorted(nums)

        
        while True:

            if nums[j-1] > nums[j]:
                j -= 1

            else:
                 
               indexElementValue = numsSorted[numsSorted.index(nums[j-1]) + 1]
               nums[j-1], nums[nums.index(indexElementValue)] = indexElementValue, nums[j-1]

               return nums[:j] + sorted(nums[j:])