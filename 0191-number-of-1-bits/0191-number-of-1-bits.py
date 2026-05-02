class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)[2:]
        y = x.count("1")
        return y