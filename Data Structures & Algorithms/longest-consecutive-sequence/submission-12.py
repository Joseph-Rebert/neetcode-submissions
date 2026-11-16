class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        max_seq = 1

        if nums == []:
            return 0
        
        for num in n:
            if num - 1 not in n:
                current_seq = 1
                while(num + current_seq) in n:
                    current_seq += 1
                max_seq = max(max_seq, current_seq)
        
        return max_seq 


        