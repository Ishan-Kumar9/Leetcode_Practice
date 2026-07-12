class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return arr
        arr1 = sorted(arr)
        res = []
        rank = {}
        rank[arr1[0]] = 1
        i = 1
        r = 1
        while i < len(arr):
            if arr1[i] != arr1[i-1]:
                r += 1
            rank[arr1[i]] = r
            i += 1

        for i in arr:
            res.append(rank[i])
        return res