class Solution(object):
    
    def isPalindrome(self, s):
        new_s = ""
        for c in s:
            if c.isalnum():
                new_s += c.lower()
        
        return new_s == new_s[::-1]


