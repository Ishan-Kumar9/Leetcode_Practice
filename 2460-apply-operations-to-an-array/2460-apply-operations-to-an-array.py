class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] += nums[i]
                nums[i+1] = 0
        
        res = [0] * len(nums)
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                res[pos] = nums[i]
                pos += 1
        return res