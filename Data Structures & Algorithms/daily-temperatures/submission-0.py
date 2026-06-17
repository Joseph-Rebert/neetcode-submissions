class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            current = temperatures[i]
            count = 1
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > current:
                    res[i] = count
                    break
                count += 1
        
        return res