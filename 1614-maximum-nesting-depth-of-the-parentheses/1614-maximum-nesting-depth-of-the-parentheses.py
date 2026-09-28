class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = maxx = 0

        for i in s:
            if i == "(":
                cnt += 1
            if i == ")":
                maxx = max(maxx, cnt)
                cnt -= 1
        return maxx