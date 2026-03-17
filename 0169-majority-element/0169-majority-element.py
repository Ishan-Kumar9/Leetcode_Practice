class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {item : nums.count(item) for item in set(nums)}
        ans = max(d, key = d.get)
        return ans