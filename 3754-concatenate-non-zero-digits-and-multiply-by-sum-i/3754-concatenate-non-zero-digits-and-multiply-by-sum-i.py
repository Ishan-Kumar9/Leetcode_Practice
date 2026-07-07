class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        s = str(n)
        x = ""
        summ = 0
        for i in s:
            if i != "0":
                x = x + i
                summ += int(i)
        return summ * int(x)    