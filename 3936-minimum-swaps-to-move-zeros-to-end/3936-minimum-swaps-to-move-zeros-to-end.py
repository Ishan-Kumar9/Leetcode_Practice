class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        while left < right:
            while left < right and nums[left] != 0:
                left += 1
            while left < right and nums[right] == 0:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                count += 1
                left += 1
                right -= 1
        return count