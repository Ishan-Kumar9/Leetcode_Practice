class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        left = 0
        window = -1
        summ = 0
        for right in range(len(nums)):
            summ += nums[right]

            while left <= right and summ > target:
                summ -= nums[left]
                left += 1

            if summ == target:
                window = max(window, right-left+1)

        if window == -1:
            return -1
        return len(nums) - window
        