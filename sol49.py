class Solution(object):
    def groupAnagrams(self, strs):

        countFreq = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in countFreq:
                countFreq[sorted_word] = []

            countFreq[sorted_word].append(word)

        return list(countFreq.values())