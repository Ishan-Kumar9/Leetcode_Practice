class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        cnt = 0
        coin = 0
        piles.sort(reverse = True)
        n = len(piles)
        x = n // 3
        i = 1
        while cnt < x:
            coin += piles[i]
            i += 2
            cnt += 1

        return coin