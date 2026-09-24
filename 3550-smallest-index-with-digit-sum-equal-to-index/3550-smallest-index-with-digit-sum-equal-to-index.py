class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            summ = 0
            temp = nums[i]
            while temp > 0:
                summ += temp%10
                temp //= 10
            if summ == i:
                return i
        return -1