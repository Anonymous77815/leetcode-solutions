from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):

        frequency = Counter(s)

        for i, char in enumerate(s):

            if frequency[char] == 1:
                return i

        return -1