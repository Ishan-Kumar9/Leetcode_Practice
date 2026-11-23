class Solution:
    def checkString(self, s: str) -> bool:
        i = 0
        n = len(s)
        while i < n:
            while i < n and s[i] == "a":
                i += 1
            while i < n and s[i] == "b":
                i += 1
            
            return i == n