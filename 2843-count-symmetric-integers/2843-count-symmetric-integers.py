class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt = 0
        for i in range(low,high+1):
            s = str(i)
            n = len(s)

            if n % 2 != 0:
                continue
            else:
                s1 = s2 = 0
                l, h = 0, n-1
                while l<h:
                    s1 += int(s[l])
                    s2 += int(s[h])
                    l += 1
                    h -= 1
                if s1 == s2:
                    cnt += 1
        return cnt