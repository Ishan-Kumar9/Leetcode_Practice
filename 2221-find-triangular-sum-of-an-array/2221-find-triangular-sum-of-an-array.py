class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        while n > 1:
            temp = []
            for i in range(n-1):
                temp.append((nums[i] + nums[i+1])%10)
            nums = temp.copy()
            n -= 1
        return nums.pop()