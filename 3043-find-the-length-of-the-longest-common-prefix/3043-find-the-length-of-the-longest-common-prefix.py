class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = set()
        maxx = 0
        for i in arr1:
            while i > 0:
                prefix.add(str(i))
                i //= 10

        for j in arr2:
            while j > 0:
                if str(j) in prefix:
                    maxx = max(maxx, len(str(j)))
                j //= 10
        return maxx