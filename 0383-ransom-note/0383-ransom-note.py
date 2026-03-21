class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = sorted(ransomNote)
        m = sorted(magazine)

        i = j = 0
        while j < len(m) and i < len(r):
            if r[i] == m[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(r)