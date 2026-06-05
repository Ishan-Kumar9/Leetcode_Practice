class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minn = float("inf")
        summ = 0
        i = 0
        n = len(nums)
        
        for j in range(n):
            summ += nums[j]
            
            while summ >= target:
                minn = min(minn, j - i + 1)
                summ -= nums[i]
                i += 1

        if minn == float("inf"):
            return 0
        return minn