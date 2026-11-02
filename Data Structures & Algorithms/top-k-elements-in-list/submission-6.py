class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)] # setup bucket sort

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for num, cnt in counts.items(): # put the nums into buckets based off frequency of it
            freq[cnt].append(num)
        
        res = []
        # go through the bucket in reverse order because we want the highest occurences
        for i in range(len(freq) -1, 0, -1):
            # look inside the individual buckets (indxs) for all its values
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            