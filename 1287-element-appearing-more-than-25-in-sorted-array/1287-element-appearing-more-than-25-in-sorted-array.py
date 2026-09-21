class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        freq = Counter(arr)
        for i in freq:
            if freq[i] > 0.25 * n:
                return i