class Solution(object):
    def plusOne(self, digits):

        j = len(digits) - 1

        while j >= 0:

            if digits[j] == 9:
                digits[j] = 0
                j -= 1

            else:
                digits[j] += 1
                return digits

        digits.insert(0, 1)

        return digits