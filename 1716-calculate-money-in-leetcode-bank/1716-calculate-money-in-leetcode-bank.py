class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        mon = 1
        while n > 6:
            ans += 28 + (7*(mon-1))
            n -= 7
            mon += 1
        while n > 0:
            ans += mon
            mon += 1
            n -= 1

        return ans