class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        perm = permutations(nums)
        res = []
        for i in perm:
            res.append(list(i))
        return res