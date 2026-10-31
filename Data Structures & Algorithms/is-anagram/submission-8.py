class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # s = sorted(s)
        # r = sorted(t)

        # if s == r:
        #     return True
        # else:
        #     return False

        count_s = {}
        count_r = {}

        for letter in s:
            if letter in count_s:
                count_s[letter] += 1
            else:
                count_s[letter] = 1

        for letter in t:
            if letter in count_r:
                count_r[letter] += 1
            else:
                count_r[letter] = 1
        
        for key, value in count_s.items():
            if key in count_r.keys():
                if count_r[key] != value:
                    return False
            else:
                return False
        
        return True
            

