class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low  = 0
        high = 1
        max_prof = 0

        while high < len(prices):
            if prices[low] < prices[high]:
                profit = prices[high] - prices[low]
                max_prof = max(max_prof, profit)
            else:
                low = high
            high += 1
        
        return max_prof
            
