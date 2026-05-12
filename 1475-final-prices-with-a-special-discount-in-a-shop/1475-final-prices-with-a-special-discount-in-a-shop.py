class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        for i in range(n):
            disc = 0
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    disc = prices[j]
                    break
            prices[i] -= disc
        return prices 