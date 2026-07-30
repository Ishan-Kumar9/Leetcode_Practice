class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        sett = set()
        i, j = 0, len(nums)-1
        while i < j:
            sett.add((nums[i]+nums[j])/2)
            i += 1
            j -= 1
        return len(sett)