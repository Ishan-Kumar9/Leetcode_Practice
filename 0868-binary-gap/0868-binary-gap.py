class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        lenn = len(s)
        if lenn < 2:
            return 0
        d = 0
        i, j = 0, 1
        while j < lenn:
            if s[j] != "1":
                j += 1
            else:
                d = max(d, j-i)
                i = j
                j += 1
        return d