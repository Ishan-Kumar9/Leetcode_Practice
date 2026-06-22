class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 0:
            if n%4 == 0:
                n //= 4
            else:
                break
        if n == 1:
            return True
        else:
            return False