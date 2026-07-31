class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        i, j = 0, len(nums)-1
        minn = float("inf")
        while i < j:
            x = (nums[i] + nums[j]) / 2
            minn = min(minn, x)
            i += 1
            j -= 1
        return minn