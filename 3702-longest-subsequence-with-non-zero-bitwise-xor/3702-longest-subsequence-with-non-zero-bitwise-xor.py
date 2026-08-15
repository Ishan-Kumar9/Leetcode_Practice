class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if n * [0] == nums:
            return 0
        
        x = 0
        for i in nums:
            x ^= i
        if x:
            return n
        return n-1