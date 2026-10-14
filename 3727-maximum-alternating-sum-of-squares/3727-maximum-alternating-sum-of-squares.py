class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            nums[i] = abs(nums[i])
        nums.sort(reverse=True)
        summ = 0
        x = 0
        if n%2 == 0:
            x += n//2
        else:
            x += n//2 + 1
        for i in range(n):
            if i < x:
                summ += nums[i]*nums[i]
            else:
                summ -= nums[i]*nums[i]
        return summ