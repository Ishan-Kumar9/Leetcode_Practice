class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        count = 0
        x1 = 32 - len(x)
        y1 = 32 - len(y)
        x = "0" * x1 + x
        y = "0" * y1 + y
        for i in range(32):
            if x[i] != y[i]:
                count += 1
        return count