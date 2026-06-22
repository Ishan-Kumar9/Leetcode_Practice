from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        res = float("inf")
        req = Counter("balloon")
        for i in req:
            if i not in freq:
                return 0
            else:
                ans = freq[i] // req[i]
                res = min(res, ans)
        return res