class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky = -1
        for i in arr:
            if i == arr.count(i):
                lucky = max(lucky, i)
        return lucky