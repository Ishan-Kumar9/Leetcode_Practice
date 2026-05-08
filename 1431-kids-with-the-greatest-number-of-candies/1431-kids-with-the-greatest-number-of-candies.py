class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        res = [True] * n
        maxx = max(candies)
        for i in range(n):
            if candies[i] == maxx:
                pass
            elif candies[i] + extraCandies < maxx:
                res[i] = False
        return res