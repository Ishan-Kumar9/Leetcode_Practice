class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxx = 0
        for j in range(len(s)-1):
            seen = set()
            count = 0
            i = j
            while i < len(s):
                if s[i] not in seen:
                    seen.add(s[i])
                    count += 1
                    maxx = max(maxx, count)
                    i += 1
                else:
                    break

        return maxx