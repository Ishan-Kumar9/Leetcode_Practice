class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        f = 0
        for i in range(n):
            f += i * nums[i]
            
        ans = f
        for j in range(1,n):
            f = f + total_sum - n * nums[-j]
            ans = max(ans, f)
        return ans