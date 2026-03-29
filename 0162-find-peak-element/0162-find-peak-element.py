class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 3:
            maxx = max(nums)
            return nums.index(maxx)
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1] and nums[i]>nums[i+1]:
                return i