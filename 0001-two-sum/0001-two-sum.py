class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            num_map[num] = i

        for i, num in enumerate(nums):
            desired = target - num
            if desired in num_map and num_map[desired] != i:
                return i, num_map[desired]
