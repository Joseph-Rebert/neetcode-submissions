class Solution(object):
    import re
    
    def isPalindrome(self, s):
        res = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
        res2 = res[::-1]
        return res == res2
        