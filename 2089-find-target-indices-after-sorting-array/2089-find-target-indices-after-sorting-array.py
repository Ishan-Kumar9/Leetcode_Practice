class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        res = []
        nums.sort()
        i = 0
        n = len(nums)
        while i < n:
            while i < n and nums[i] != target:
                i += 1

            while i < n and nums[i] == target:
                res.append(i)
                i += 1
            return res