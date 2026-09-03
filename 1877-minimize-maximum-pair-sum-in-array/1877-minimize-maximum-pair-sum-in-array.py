class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxx = 0
        nums.sort()
        i, j = 0, len(nums)-1
        while i < j:
            maxx = max(maxx, nums[i]+nums[j])
            i += 1
            j -= 1
        return maxx