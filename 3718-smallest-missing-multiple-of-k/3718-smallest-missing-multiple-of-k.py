class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sett = set(nums)
        for i in range(1, n+2):
            if k * i not in sett:
                return k * i