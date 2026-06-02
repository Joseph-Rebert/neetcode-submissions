class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        result = set()

        print(result)
        for i in range(len(sorted_nums)):
            l, r = i + 1, len(sorted_nums) - 1
            target = sorted_nums[i] * -1
            while l < r:
                if sorted_nums[l] + sorted_nums[r] == target:
                    result.add((sorted_nums[i], sorted_nums[l], sorted_nums[r]))
                    l += 1
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < target:
                    l += 1
                elif sorted_nums[l] + sorted_nums[r] > target:
                    r -= 1
            
        return [list(triplet) for triplet in result]

