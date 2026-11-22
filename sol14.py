class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        
        firstWord = strs[0]

        for i in range(len(firstWord)):
            char = firstWord[i]

            for word in strs[1:]:

                if char != word[i] or i == len(word):

                    return firstWord[:i]


        return firstWord

