class Solution:
    def reverseDegree(self, s: str) -> int:
        d = {letter: 26 - idx for idx, letter in enumerate(string.ascii_lowercase)}
        ans = 0
        for i in range(len(s)):
            ans += d[s[i]] * (i+1)
        return ans