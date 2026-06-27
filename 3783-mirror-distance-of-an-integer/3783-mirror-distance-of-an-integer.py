class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev = 0
        temp = n
        while n > 0:
            ld = n % 10
            rev = rev * 10 + ld
            n //= 10
        ans = abs(temp - rev)
        return ans