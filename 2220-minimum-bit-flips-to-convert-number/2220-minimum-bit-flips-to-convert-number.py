class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s = bin(start)[2:]
        g = bin(goal)[2:]
        if len(s) > len(g):
            d = len(s) - len(g)
            g = "0"*d + g
        else:
            d = len(g) - len(s)
            s = "0"*d + s

        cnt = 0
        for i in range(len(g)):
            if s[i] != g[i]:
                cnt += 1
        return cnt