class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                maxx = max(maxx, count)
            else:
                count = 0
        return maxx