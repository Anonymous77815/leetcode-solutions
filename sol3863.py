class Solution(object):
    def minOperations(s):

        is_sorted = True
        for i in range(len(s) - 1):
            if s[i] > s[i + 1]:
                is_sorted = False
                break
        if is_sorted:
            return 0


        if len(s) == 2:
            return -1

        min_char = min(s)
        max_char = max(s)

        if s[0] == min_char or s[-1] == max_char:
            return 1

        if min_char in s[1:-1] or max_char in s[1:-1]:
            return 2

        return 3