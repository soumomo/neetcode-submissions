class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        difference = 0
        for R in range(1, len(prices)):
            if prices[L] > prices[R]:
                L = R
                R += 1
            else:
                difference = max(difference, prices[R] - prices[L])
                R += 1
        return difference


        