class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max1 = -1
        max2 = -1
        for i in range(len(nums)):
            if max1 == -1 or nums[i] > nums[max1]:
                max2 = max1
                max1 = i
            elif max2 == -1 or nums[i] > nums[max2]:
                max2 = i
        if nums[max1] >= 2 * nums[max2]:
            return max1
        return -1