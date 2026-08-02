class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        even = odd = 0
        for i in range(len(piles)):
            if i % 2 == 0:
                even += piles[i]
            else:
                odd += piles[i]
        return True