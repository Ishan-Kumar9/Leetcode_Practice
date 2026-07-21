class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        mid = len(nums)//2

        if nums[mid] in nums[:mid] or nums[mid] in nums[mid+1:]:
            return False
        return True