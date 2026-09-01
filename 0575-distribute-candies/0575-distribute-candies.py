class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        sett = set(candyType)
        return min(n//2, len(sett))