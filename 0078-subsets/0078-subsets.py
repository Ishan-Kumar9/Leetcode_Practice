from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        n = 1
        while n < len(nums)+1:
            
            for i in combinations(nums, n):
                res.append(list(i))
            n += 1
        return res