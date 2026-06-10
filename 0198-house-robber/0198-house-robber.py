class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #if n == 1: return nums[0]
        #if n == 2: return max(nums)
        ans = [0]*n
        
        for i in range(n):
            if i == 0:
                ans[i] = nums[0]
            elif i == 1:
                ans[i] = max(nums[0], nums[1])
            else:
                ans[i] = max(ans[i-2] + nums[i], ans[i-1])

        return ans[-1]