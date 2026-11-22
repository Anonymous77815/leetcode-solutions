class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)

        i = 0
        j = 0
        maxLen = 0

        while j < len(s):
            if j + 1 < len(s) and s[j + 1] not in s[i:j + 1]:
                j += 1
            else:
                maxLen = max(maxLen, len(s[i:j + 1]))
                i += 1
                j = i

        return maxLen