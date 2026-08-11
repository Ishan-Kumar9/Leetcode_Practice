from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        n = len(nums) / 3
        res = []
        for k, v in freq.items():
            if v > n:
                res.append(k)
        return res