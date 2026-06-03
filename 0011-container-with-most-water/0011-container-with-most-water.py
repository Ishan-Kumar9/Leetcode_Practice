class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        h = len(height)-1
        maxx = -float("inf")
        while l < h:
            if height[l] <= height[h]:
                ans = height[l] * (h - l)
                maxx = max(maxx, ans)
                l += 1
            else:
                ans = height[h] * (h - l)
                maxx = max(maxx, ans)
                h -= 1
        return maxx