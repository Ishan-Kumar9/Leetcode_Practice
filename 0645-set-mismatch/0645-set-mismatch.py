class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set(range(1,n+1))
        wrong = set(nums)
        nums.sort()
        x = (s-wrong).pop()
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return [nums[i], x]