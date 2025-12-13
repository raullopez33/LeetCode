class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # going to do a sliding window approach to only go 
        #O(n) since the brute force is O(n**2)

        #Our invariant 
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP
