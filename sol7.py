class Solution(object):
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        x = abs(x)

        reversedNum = 0

        while x > 0:

            dig = x % 10
            reversedNum = reversedNum * 10 + dig
            x = x // 10

        reversedNum *= sign

        if reversedNum > 2**31 - 1 or reversedNum < -2**31:
            return 0

        return reversedNum