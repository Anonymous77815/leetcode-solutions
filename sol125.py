class Solution(object):
    def isPalindrome(self, s):

        s = ''.join(char.lower() for char in s if char.isalnum())

        j = len(s)-1
        i = 0

        while i < len(s)//2:
        
                        if s[i] == s[j]:
                            i+=1
                            j-=1
        
                        else:
                            return False
        return True
                
                

            