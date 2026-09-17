class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## Problem Restatement: You are given an array of integers representing the price of NeetCoin on the ith (index) day. You need to return the maxmium profit you can achieve by choosing a day to buy and a DIFFERENT day to sell

        ## Brute Force: Use two for-loops one iterates through the array once and the inner-for-loop runs every time the outer one iterates. It will keep calculating the profit everytime until it finds the greatest output. This would give us an O(n^2) time complexity.

        ## More Optimized Solution: two pointers where one pointer only moves if the value of the item that the other pointer is pointing to is < than the first one. Keep calculating the profit and comparing it with max profit

        maxProf = 0
        first = 0
        sec = 1

        while sec < len(prices):
            maxProf = max(maxProf, prices[sec] - prices[first])
            if prices[first] > prices[sec]:
                first = sec
            
            sec += 1
        
        return maxProf
            