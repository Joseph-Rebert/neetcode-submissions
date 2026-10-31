class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}

        for i in range(len(nums)):
            temp_target = target - nums[i]
            
            if temp_target in counts:
                return [counts[temp_target], i]
            
            counts[nums[i]] = i
            

        