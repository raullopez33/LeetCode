class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # going to do a sliding window approach to only go 
        #O(n) since the brute force is O(n**2)

        #Our invariant 
        l = 0
        max_p = 0

        for r in range(1, len(prices)):

            if prices[r] < prices[l]:
                l = r
            else:
                max_p = max(max_p, prices[r]-prices[l])
        
        return max_p