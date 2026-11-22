def trap(height):

    total_water = 0
    stack = []

    for i in range(len(height)):
        while stack and height[i]>height[stack[-1]]:
            bottom = stack.pop()

            if not stack:
                break

            left = stack[-1]
            right = i

            width = right - left -1
            bounded_height = min(height[left], height[right]) - height[bottom]

            total_water += width*bounded_height

        stack.append(i)

    return total_water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))