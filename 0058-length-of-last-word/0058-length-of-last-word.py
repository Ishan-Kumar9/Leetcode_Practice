class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        n = len(s)
        i = n-1
        count = 0
        while s[i] == " " and i>=0:
            i -= 1

        while s[i] != " " and i>=0:
            count += 1
            i -= 1

        return count