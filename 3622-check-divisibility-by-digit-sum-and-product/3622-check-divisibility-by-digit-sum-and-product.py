class Solution:
    def checkDivisibility(self, n: int) -> bool:
        summ = 0
        prod = 1
        temp = n
        while n > 0:
            ld = n%10
            summ += ld
            prod *= ld
            n //= 10
        return temp % (summ + prod) == 0