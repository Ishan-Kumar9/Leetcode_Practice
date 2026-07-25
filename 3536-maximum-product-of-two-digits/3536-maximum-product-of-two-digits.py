class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = 0
        max2 = 0
        while n > 0:
            ld = n % 10
            if ld > max1:
                max2 = max1
                max1 = ld
            elif ld > max2:
                max2 = ld
            n //= 10
        return max1 * max2