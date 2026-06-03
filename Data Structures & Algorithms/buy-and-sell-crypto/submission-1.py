class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l , r = 0, 1

        while r < len(prices):
            current_profit = prices[r] - prices[l]

            # if right is greater than left
            if prices[l] > prices[r]:
                l = r
                r += 1
            else:
                r += 1
            
            max_profit = max(current_profit, max_profit)

        return max_profit   