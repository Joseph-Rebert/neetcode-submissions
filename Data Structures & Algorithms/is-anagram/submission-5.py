class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occurences= {}
        for character in s:
            if character in occurences:
                occurences[character] += 1
            else:
                occurences[character] = 1
        
        for character in t:
            if character in occurences:
                occurences[character] -= 1
                
                if occurences[character] == 0:
                    occurences.pop(character)
            
            else:
                return False
        
        if occurences == {}:
            return True
        else:
            return False
