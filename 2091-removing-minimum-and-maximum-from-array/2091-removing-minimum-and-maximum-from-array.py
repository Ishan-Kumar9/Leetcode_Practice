class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minn = nums.index(min(nums))
        maxx = nums.index(max(nums))

        begin = max(minn+1, maxx+1)
        end = len(nums) - min(minn, maxx)
        both = min(minn+1, maxx+1) + len(nums) - max(minn, maxx)
        return min(begin, end, both)