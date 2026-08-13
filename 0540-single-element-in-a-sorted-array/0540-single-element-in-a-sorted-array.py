class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        i = 0
        while i < n-1:
            if nums[i] == nums[i+1]:
                    i += 2
            else:
                return nums[i]
            if i == n-1:
                return nums[i]