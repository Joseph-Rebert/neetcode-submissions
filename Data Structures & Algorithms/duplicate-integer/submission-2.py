class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
    
        if len(nums) == 0:
            return False
    
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = 0

        return False
            
        