class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        if n < 2:
            return False
        res = [0, 1, 1]
        p = 0
        while res[-1] < n:
            res.append(res[-1] + res[-2])
            if res[-1] + res[p] == n:
                return True
            else:
                p += 1
        return False