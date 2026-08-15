class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = nums[0]
        zero = True
        for i in range(1,len(nums)):
            ans = ans ^ nums[i]
            if nums[i] != 0:
                zero = False

        if ans != 0:
            return len(nums)
        else:
            if zero:
                return 0
            else:
                return len(nums)-1 