def threeSumClosest(nums, target):
    nums.sort()
    minDiffernece = float('inf')
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            closestSum = nums[i] + nums[left] + nums[right]
            if closestSum == target:
                return target
            elif closestSum < target:
                if minDiffernece > target - closestSum:
                    minDiffernece = target - closestSum
                left += 1
            else:
                if minDiffernece > closestSum - target:
                    minDiffernece = closestSum - target
                right -= 1

    return target - minDiffernece
print(threeSumClosest([-1, 2, 1, -4], 1))