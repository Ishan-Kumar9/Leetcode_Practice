class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = n*(n+1)
        odd = n**2

        return even - odd