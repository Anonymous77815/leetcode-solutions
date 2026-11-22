#This is a slow solution wiht time complexity of O(n^2) and space complexity of O(n^2)

# def mostwater(heightarr):
#     i = 0
    
    
#     arealist = []
#     for i in range(len(heightarr)):
#         for j in range(i+1, len(heightarr)):
#             arealist.append(min(heightarr[i], heightarr[j]) * (j - i))

#     return max(arealist)

# print(mostwater([1,8,6,2,5,4,8,3,7]))

#time complexity of O(n) and space complexity of O(1)
def mostwater(heightarr):
    left = 0
    right = len(heightarr) - 1
    maxarea = 0
    while left < right:
        area = min(heightarr[left], heightarr[right]) * (right - left)
        maxarea = max(maxarea, area)

        if heightarr[left] < heightarr[right]:
            left += 1
        else:
            right -= 1
    return maxarea