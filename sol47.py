class Solution(object):
    def permuteUnique(self, nums):

        nums.sort()
        current = []
        result = []
        used = [False]*len(nums)

        def backtrack():


            if len(nums) == len(current):
                result.append(current[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                current.append(nums[i])
                used[i] = True
                backtrack()


                current.pop()
                used[i] = False

        backtrack()

        return result