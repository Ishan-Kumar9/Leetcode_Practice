class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        s_x = str(x)
        if s_x in s:
            if s[0] != s_x:
                return True
        return False