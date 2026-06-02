class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = 1

        while True:
            if numbers[l] + numbers[r] == target:
                return [l + 1,r + 1]

            if r == len(numbers) - 1:
                l += 1
                r = l + 1
            else:
                r += 1