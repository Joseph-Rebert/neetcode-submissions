class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        if len(nums) == 0:
            return False
        
        for item in nums:
            if dic.__contains__(item):
                return True
            else:
                dic[item] = 1
        return False
            
        