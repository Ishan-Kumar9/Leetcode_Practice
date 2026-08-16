class Solution:
    def canAliceWin(self, n: int) -> bool:
        i = 10
        flag = False
        while n > 0:
            if n < i:
                return flag
            else:
                if i % 2 == 0:
                    flag = True
                else:
                    flag = False
                n -= i
                i -= 1
        return flag