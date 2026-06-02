class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            number_needed = target - nums[i]
            if number_needed in dic:
                return [dic[number_needed], i]
            else:
                dic[nums[i]] = i