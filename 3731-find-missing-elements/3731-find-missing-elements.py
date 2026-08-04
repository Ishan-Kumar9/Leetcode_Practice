class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        maxx = max(nums)
        minn = min(nums)

        required = list(range(minn, maxx+1))
        return sorted(list(set(required) - set(nums)))