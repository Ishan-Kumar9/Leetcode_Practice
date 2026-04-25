class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxx = 0
        n = len(colors)
        for i in range(n):
            for j in range(n):
                if colors[i] != colors[j]:
                    d = abs(i-j)
                    maxx = max(maxx, d)
        return maxx