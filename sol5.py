class Solution(object):
    def longestPalindrome(self, s):

        result = ""

        for mid in range(len(s)):

            i, j = mid, mid

            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > len(result):
                    result = s[i:j+1]
                i -= 1
                j += 1

            i, j = mid, mid + 1

            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i + 1 > len(result):
                    result = s[i:j+1]
                i -= 1
                j += 1

        return result