

def largestRectangleArea(height):
        stack = []
        max_h = 0

        height.append(0)

        for i in range(len(height)):

            while stack and height[stack[-1]] > height[i]:

                index = stack.pop()

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height[index] * width

                max_h = max(max_h, area)

            stack.append(i)

        return max_h

print(largestRectangleArea([2,3,4,5]))