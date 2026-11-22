def subsets(nums):

    path = []
    result = []

    def backtracking(index):

        if index == len(nums):
            result.append(path[:])
            return

        path.append(nums[index])
        backtracking(index+1)

        path.pop()
        backtracking(index+1)


    backtracking(0)


    return result