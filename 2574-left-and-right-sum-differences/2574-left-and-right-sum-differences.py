class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        right = sum(nums)
        left = 0
        for i in range(n):
            left += nums[i]
            answer[i] = abs(right-left)

            right -= nums[i]

        return answer