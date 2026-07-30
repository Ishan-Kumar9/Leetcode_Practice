class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans = 0
        if n < 9:
            return n
        elif n < 17:
            return 8 + (n-8)*2
        elif n < 25:
            return 24 + (n-16)*3
        else:
            return 48 + (n-24)*4