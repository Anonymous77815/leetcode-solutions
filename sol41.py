def firstMissingPositive(nums):

    numSet = set(nums)
    minNum = float('inf')
    j = 0

    for i in range(len(nums)):

        if nums[i] > 0:
            minNum = min(minNum, nums[i])
            j +=1


    if minNum != 1:
        return 1
    else:
        k=1
        while True:
            if minNum + k not in numSet:
                return minNum+k
            else:
                j+=1