def search(nums, target):
    newnums = sorted(nums)
    left, right = 0, len(newnums) - 1
    while left <= right:
        mid = (left + right) // 2
        if newnums[mid] == target:
            break
        elif newnums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if target in nums:
        return True
    else:
        return False

print(search([4,5,6,7,0,1,2], 0))