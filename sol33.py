def search(nums, target):
    newnums = nums[:]
    nums.sort()
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return newnums.index(target)
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1


    return -1

print(search([4,5,6,7,0,1,2], 0)) 