class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        b = bin(n)[2:]
        x = b.count("11")
        y = b.count("111")
        return x == 1 and y == 0