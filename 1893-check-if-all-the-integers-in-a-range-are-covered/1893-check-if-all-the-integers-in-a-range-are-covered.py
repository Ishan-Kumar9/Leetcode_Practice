class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        req = list(range(left, right+1))
        seen = set()
        for i in range(len(req)):
            for j in ranges:
                if j[0] <= req[i] <= j[1]:
                    seen.add(req[i])
        return req == sorted(list(seen))
                