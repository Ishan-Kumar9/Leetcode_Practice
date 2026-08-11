class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        n = len(nums) / 3
        res = []
        for i in freq:
            if freq[i] > n:
                res.append(i)
        return res