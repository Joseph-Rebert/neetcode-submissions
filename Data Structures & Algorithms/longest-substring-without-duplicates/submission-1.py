class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        l = 0
        longest_sub_str = 0

        for r in range(len(s)):
            if s[r] in dic:
                l = max(dic[s[r]] + 1, l)
            dic[s[r]] = r
            longest_sub_str = max(longest_sub_str, r - l + 1)
        
        return longest_sub_str


