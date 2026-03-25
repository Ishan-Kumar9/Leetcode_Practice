class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        total = 0
        curr = 0

        for i in range(len(nums)-1):
            total = max(total, i + nums[i])
            if i == curr:
                jumps += 1
                curr = total

        return jumps