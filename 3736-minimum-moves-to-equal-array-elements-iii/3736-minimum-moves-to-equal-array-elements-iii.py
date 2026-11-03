class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        summ = 0
        for i in nums:
            summ += mx - i
        return summ