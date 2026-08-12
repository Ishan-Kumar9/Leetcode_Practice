class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        maxx = 0
        start = -1

        for i in range(len(nums)):
            freq[nums[i]] += 1
            while freq[nums[i]] > k:
                start += 1
                freq[nums[start]] -= 1
                maxx = max(maxx, i-start)
        maxx = max(maxx, i-start)
        return maxx