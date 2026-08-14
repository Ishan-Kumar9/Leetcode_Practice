class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        maxx = 0
        for i in range(len(s)):
            seen = {}
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen[s[j]] = 1
                else:
                    seen[s[j]] += 1
                if seen[s[j]] == 3:
                    maxx = max(maxx, (j-i))
                    break
                if j == len(s)-1:
                    maxx = max(maxx, (j-i+1))
        return maxx