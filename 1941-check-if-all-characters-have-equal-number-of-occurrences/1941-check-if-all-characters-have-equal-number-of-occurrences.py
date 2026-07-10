from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        freq = Counter(s)
        for i in freq.values():
            if i != freq[s[0]]:
                return False
        return True