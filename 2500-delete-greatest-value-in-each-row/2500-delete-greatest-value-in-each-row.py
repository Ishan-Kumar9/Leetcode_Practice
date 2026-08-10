class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for i in grid:
            i.sort(reverse = True)

        for j in range(n):
            maxx = 0
            for k in range(m):
                maxx = max(maxx, grid[k][j])
            ans += maxx
        return ans