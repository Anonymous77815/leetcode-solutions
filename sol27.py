class Solution(object):
    def removeElement(self,nums, val):

        if len(nums) == 1:
            if nums[0] == val:
                return []
            else:
                return nums

        n = len(nums)-1
        i=0
        j=0

        while j < n:

            if nums[i] == val:
                popVal = nums.pop(i)
                nums.append(popVal)
            else:
                i += 1

            j += 1

        return i
