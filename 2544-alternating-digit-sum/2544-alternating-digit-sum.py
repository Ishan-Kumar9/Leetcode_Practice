class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        summ = 0
        for i in range(len(s)):
            d = int(s[i])
            if i % 2 == 0:
                summ += d
            else:
                summ -= d
        return summ