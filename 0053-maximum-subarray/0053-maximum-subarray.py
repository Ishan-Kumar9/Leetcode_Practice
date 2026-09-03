class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = - float("inf")
        curr = 0
        for right in range(len(nums)):
            curr += nums[right]
            if curr < nums[right]:
                curr = nums[right]
            maxx = max(maxx, curr)
        return maxx