class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        org = n
        for i in range(t):
            n = org + i
            p = 1
            while n > 0:
                p *= (n % 10)
                n //= 10

            if p%t == 0:
                return org + i