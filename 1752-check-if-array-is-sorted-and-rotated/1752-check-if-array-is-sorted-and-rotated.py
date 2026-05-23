class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)-1
        r = sorted(nums)
        if nums == r:
            return True
        i = 0
        while i < n:
            if nums[i] > nums[i+1]:
                res = nums[i+1:] + nums[:i+1]
                return r == res
            i += 1