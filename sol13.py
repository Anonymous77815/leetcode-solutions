
class Solution(object):
    def romanToInt(self, s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        i = 0

        while i < len(s):
            if i + 1 < len(s) and s[i] == "I" and s[i+1] == "V":
                result += 4
                i += 2
            elif i + 1 < len(s) and s[i] == "I" and s[i+1] == "X":
                result += 9
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i+1] == "L":
                result += 40
                i += 2
            elif i + 1 < len(s) and s[i] == "X" and s[i+1] == "C":
                result += 90
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i+1] == "D":
                result += 400
                i += 2
            elif i + 1 < len(s) and s[i] == "C" and s[i+1] == "M":
                result += 900
                i += 2
            else:
                result += roman[s[i]]
                i += 1

        return result
